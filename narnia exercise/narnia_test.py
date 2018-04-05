from narnia import Wardrobe, Narnia
import unittest


class TestWardrobe(unittest.TestCase):
    def setUp(self):
        pass

    def test_kick(self):
        w = Wardrobe("wood", "billy")
        self.assertEqual(w.kick(), "'Boem!'")
        w.material = "carbon"
        self.assertEqual(w.kick(), "'Tok!'")
        w.material = "glass"
        self.assertEqual(w.kick(), "'Ting!'")
        w.material = "j3p19"
        self.assertEqual(
            w.kick(), "can't kick the closet your closet is made out of a kick-resistant material!")


class TestNarnia(unittest.TestCase):
    def setUp(self):
        pass

    def visit(self):
        n = Narnia(0, "kees")
        self.assertIsNone(n.visit())


if __name__ == '__main__':
    unittest.main(verbosity=3)
