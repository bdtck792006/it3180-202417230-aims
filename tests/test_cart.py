import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Star Wars"],
        )

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [18.99, 24.95],
        )
    def test_add_dvd_until_full(self):
        cart = Cart()

        for index in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {index + 1}")
            self.assertTrue(cart.add_dvd(dvd))

        extra_dvd = DigitalVideoDisc("Extra DVD")
        self.assertFalse(cart.add_dvd(extra_dvd))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_discount_returns_remaining_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100))

        self.assertAlmostEqual(
            cart.total_cost_with_discount(20), 80
        )

    def test_discount_rejects_invalid_percent(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
    def test_discount_rejects_negative_percent(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)

if __name__ == "__main__":
    unittest.main()