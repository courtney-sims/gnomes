import unittest

from gnomes import Gnomes

class TestGnomes(unittest.TestCase):
    def test_appease(self):
        gnome = Gnomes()
        self.assertTrue(gnome.check_appeasement(4))
    
    def test_appease_displeased(self):
        gnome = Gnomes()
        self.assertFalse(gnome.check_appeasement(-1))

    def test_calculate_score(self):
        gnome = Gnomes()
        self.assertEqual(3, gnome.calculate_score('fuzzy socks'))

if __name__ == '__main__':
	unittest.main()
