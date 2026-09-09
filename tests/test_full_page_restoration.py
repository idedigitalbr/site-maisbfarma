import unittest

from playwright.sync_api import sync_playwright

from tests.test_category_section import local_site


class FullPageRestorationTests(unittest.TestCase):
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

    def test_restores_the_approved_google_testimonials_section(self):
        heading = self.page.get_by_role(
            "heading", name="O que nossos clientes dizem no Google."
        )
        self.assertEqual(heading.count(), 1)
        self.assertEqual(
            self.page.get_by_role("heading", name="Luciana Nascimento").count(), 1
        )
        self.assertEqual(
            self.page.get_by_text(
                '"Ótimo atendimento e preços muito bons"', exact=True
            ).count(),
            1,
        )

    def test_restores_the_approved_store_and_footer_layout(self):
        stores = self.page.locator("#filiais")
        self.assertEqual(stores.count(), 1)
        self.assertEqual(stores.get_by_text("Prefere falar com a gente?").count(), 0)
        self.assertEqual(
            self.page.get_by_text(
                "Farmácia do grupo +B, feita para cuidar da sua saúde com confiança no atendimento.",
                exact=True,
            ).count(),
            1,
        )

    def test_horizontal_banner_controls_move_the_approved_carousel(self):
        track = self.page.locator("#hBannersTrack")
        next_button = self.page.get_by_role("button", name="Próximo banner")
        self.assertEqual(track.count(), 1)
        self.assertEqual(next_button.count(), 1)

        before = track.evaluate("element => getComputedStyle(element).transform")
        next_button.click()
        self.page.wait_for_timeout(400)
        after = track.evaluate("element => getComputedStyle(element).transform")
        self.assertNotEqual(after, before)

    def test_uses_the_three_existing_hero_images(self):
        expected_sources = [
            "assets/Pagina/S1%20TOPO%20HERO/1-banner-topo.webp",
            "assets/Pagina/S1%20TOPO%20HERO/2-banner-topo.webp",
            "assets/Pagina/S1%20TOPO%20HERO/3-banner-topo.webp",
        ]
        images = self.page.locator("#home .hero-slide > img")
        self.assertEqual(images.count(), 3)
        self.assertEqual(images.evaluate_all("items => items.map(item => item.getAttribute('src'))"), expected_sources)
        self.assertTrue(
            images.evaluate_all(
                "items => items.every(item => item.complete && item.naturalWidth > 0)"
            )
        )


if __name__ == "__main__":
    unittest.main()
