from narnia import Wardrobe
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


if __name__ == '__main__':
    unittest.main(verbosity=3)

# w = Wardrobe("wood", "billy")
# # print(w.open())
# # print(w.close())
# # print(w.get_in())
# # print(w.open())
# # print(w.get_in())
# # print(w.close())
# # print(w.get_out())
# print(w)
# print(w.kick())
