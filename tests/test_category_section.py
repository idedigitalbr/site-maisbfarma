import contextlib
import http.server
import socket
import threading
import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass


@contextlib.contextmanager
def local_site():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]

    handler = lambda *args, **kwargs: QuietHandler(
        *args, directory=str(PROJECT_ROOT), **kwargs
    )
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}/index.html"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


class CategorySectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = local_site()
        cls.url = cls.site.__enter__()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.site.__exit__(None, None, None)

    def setUp(self):
        self.page = self.browser.new_page(viewport={"width": 1440, "height": 1000})
        self.page.goto(self.url, wait_until="domcontentloaded")

    def tearDown(self):
        self.page.close()

    def test_displays_the_ten_reference_categories_as_loaded_circles(self):
        expected_names = [
            "Infantil",
            "Dermocosméticos",
            "Higiene Pessoal",
            "Beleza e Cuidados",
            "Medicamentos",
            "Mercado",
            "Saúde e Bem-Estar",
            "Nutrição Saudável",
            "Pet Shop",
            "e muito mais....",
        ]
        items = self.page.locator("#categorias [data-category-item]")
        self.assertEqual(items.count(), 10)
        rendered_names = [" ".join(name.split()) for name in items.all_inner_texts()]
        self.assertEqual(rendered_names, expected_names)

        loaded_circles = items.locator("img").evaluate_all(
            """images => images.every(image => {
                const style = getComputedStyle(image);
                return image.complete && image.naturalWidth > 0
                    && style.borderRadius === '9999px';
            })"""
        )
        self.assertTrue(loaded_circles)

    def test_categories_are_rendered_before_hero_section(self):
        visual_order = self.page.evaluate(
            """() => ({
                categoriesTop: document.querySelector('#categorias').offsetTop,
                heroTop: document.querySelector('#home').offsetTop,
            })"""
        )
        self.assertLess(visual_order["categoriesTop"], visual_order["heroTop"])

    def test_category_opens_the_existing_order_picker(self):
        category = self.page.get_by_role("button", name="Comprar produtos da categoria Infantil")
        self.assertEqual(category.count(), 1)
        category.click()
        self.assertTrue(self.page.locator("#orderModal").is_visible())

    def test_each_category_label_stays_inside_its_button(self):
        labels_fit = self.page.locator("#categorias [data-category-item]").evaluate_all(
            """items => items.every(item => {
                const itemRect = item.getBoundingClientRect();
                const labelRect = item.querySelector('.category-label').getBoundingClientRect();
                return labelRect.bottom <= itemRect.bottom + 0.5;
            })"""
        )
        self.assertTrue(labels_fit)

    def test_no_navigation_arrows_and_badges_are_white_with_red_icons(self):
        nav_buttons = self.page.locator(".category-nav")
        self.assertEqual(nav_buttons.count(), 0)

        badges_style = self.page.locator("#categorias .category-icon-badge").evaluate_all(
            """badges => badges.map(badge => {
                const style = getComputedStyle(badge);
                return {
                    bg: style.backgroundColor,
                    color: style.color,
                };
            })"""
        )
        self.assertEqual(len(badges_style), 10)
        for badge in badges_style:
            self.assertEqual(badge["bg"], "rgb(248, 249, 250)")
            self.assertEqual(badge["color"], "rgb(233, 33, 37)")

    def test_mobile_displays_single_row_horizontal_scroll_for_categories(self):
        self.page.set_viewport_size({"width": 390, "height": 844})
        self.page.reload(wait_until="domcontentloaded")

        dimensions = self.page.evaluate(
            """() => {
                const rail = document.querySelector('#categoryRail');
                const items = Array.from(document.querySelectorAll('#categorias [data-category-item]'));
                const offsets = items.map(item => item.offsetTop);
                const allSameTop = offsets.every(top => Math.abs(top - offsets[0]) < 4);
                return {
                    pageWidth: document.documentElement.scrollWidth,
                    viewportWidth: window.innerWidth,
                    railScrollWidth: rail.scrollWidth,
                    railClientWidth: rail.clientWidth,
                    allSameTop: allSameTop,
                };
            }"""
        )
        # O layout geral não deve ter scroll horizontal indesejado
        self.assertLessEqual(dimensions["pageWidth"], dimensions["viewportWidth"])
        # O rail de categorias deve ser rolável horizontalmente
        self.assertGreater(dimensions["railScrollWidth"], dimensions["railClientWidth"])
        # Todos os 10 itens devem estar na MESMA linha (mesmo offsetTop)
        self.assertTrue(dimensions["allSameTop"])

    def test_mobile_hero_navigation_arrows_are_hidden(self):
        # No mobile (390px), as setas do Hero Carrossel NÃO devem ser visíveis para não cobrir o texto
        self.page.set_viewport_size({"width": 390, "height": 844})
        self.page.reload(wait_until="domcontentloaded")
        hero_arrows = self.page.locator(".hero-nav-btn")
        for i in range(hero_arrows.count()):
            self.assertFalse(hero_arrows.nth(i).is_visible())

        # No desktop (1440px), as setas DEVEM ser visíveis
        self.page.set_viewport_size({"width": 1440, "height": 900})
        self.page.reload(wait_until="domcontentloaded")
        hero_arrows_desktop = self.page.locator(".hero-nav-btn")
        self.assertEqual(hero_arrows_desktop.count(), 2)
        for i in range(hero_arrows_desktop.count()):
            self.assertTrue(hero_arrows_desktop.nth(i).is_visible())


if __name__ == "__main__":
    unittest.main()
