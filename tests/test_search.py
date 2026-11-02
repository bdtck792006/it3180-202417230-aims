import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_ignores_case(self):
        dvd = DigitalVideoDisc("The Lion King")

        result = search_by_title([dvd], "lion")

        self.assertEqual(result, [dvd])


if __name__ == "__main__":
    unittest.main()