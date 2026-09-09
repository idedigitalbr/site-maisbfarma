import unittest
from playwright.sync_api import sync_playwright
from tests.test_category_section import local_site


class HeaderNavigationTests(unittest.TestCase):
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

    def test_desktop_navigation_layout_and_icons(self):
        page = self.browser.new_page(viewport={'width': 1440, 'height': 900})
        page.goto(self.url, wait_until='domcontentloaded')

        logo = page.locator('.header-logo')
        self.assertEqual(logo.count(), 1)
        self.assertTrue(logo.is_visible())

        inner_box = page.locator('.header-inner').bounding_box()
        logo_box = logo.bounding_box()
        self.assertIsNotNone(inner_box)
        self.assertIsNotNone(logo_box)
        inner_center_x = inner_box['x'] + inner_box['width'] / 2
        logo_center_x = logo_box['x'] + logo_box['width'] / 2
        self.assertAlmostEqual(inner_center_x, logo_center_x, delta=15)

        nav_left = page.locator('#nav-left')
        self.assertTrue(nav_left.is_visible())
        left_links = nav_left.locator('.nav-link')
        self.assertEqual(left_links.count(), 3)

        expected_left = ['Início', 'Sobre', 'Nossas Lojas']
        for idx, text in enumerate(expected_left):
            link = left_links.nth(idx)
            self.assertIn(text, link.inner_text())
            self.assertEqual(link.locator('svg').count(), 1)

        nav_right = page.locator('#nav-right')
        self.assertTrue(nav_right.is_visible())
        right_links = nav_right.locator('.nav-link')
        self.assertEqual(right_links.count(), 1)

        expected_right = ['Ofertas']
        for idx, text in enumerate(expected_right):
            link = right_links.nth(idx)
            self.assertIn(text, link.inner_text())
            self.assertEqual(link.locator('svg').count(), 1)

        cta_order = nav_right.locator('.nav-btn-order')
        self.assertTrue(cta_order.is_visible())
        self.assertIn('Pedir agora', cta_order.inner_text())
        self.assertEqual(cta_order.locator('svg').count(), 1)

        toggle = page.locator('#mobileMenuBtn')
        self.assertFalse(toggle.is_visible())

        page.close()

    def test_mobile_navigation_and_drawer_interaction(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 667})
        page.goto(self.url, wait_until='domcontentloaded')

        self.assertFalse(page.locator('#nav-left').is_visible())
        self.assertFalse(page.locator('#nav-right').is_visible())

        toggle = page.locator('#mobileMenuBtn')
        self.assertTrue(toggle.is_visible())

        logo = page.locator('.header-logo')
        self.assertTrue(logo.is_visible())

        mobile_cta = page.locator('.header-mobile-cta')
        self.assertTrue(mobile_cta.is_visible())

        drawer = page.locator('#mobileMenu')
        self.assertFalse(drawer.is_visible())

        toggle.click()
        page.wait_for_timeout(350)
        self.assertTrue(drawer.is_visible())
        self.assertIn('is-open', drawer.get_attribute('class'))

        drawer_links = drawer.locator('.drawer-link')
        self.assertGreaterEqual(drawer_links.count(), 6)

        close_btn = page.locator('.mobile-drawer-close')
        close_btn.click()
        page.wait_for_timeout(350)
        self.assertNotIn('is-open', drawer.get_attribute('class'))

        page.close()


if __name__ == '__main__':
    unittest.main()
