import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]

        result = search_by_category(items, "Animation")

        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Aladdin"],
        )

    def test_search_by_category_no_match(self):
        items = [DigitalVideoDisc("The Lion King", "Animation")]

        self.assertEqual(search_by_category(items, "Comedy"), [])

    def test_search_by_title_ignores_case(self):
        dvd = DigitalVideoDisc("The Lion King")

        result = search_by_title([dvd], "lion")

        self.assertEqual(result, [dvd])


if __name__ == "__main__":
    unittest.main()