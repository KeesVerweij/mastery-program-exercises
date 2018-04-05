from narnia import Wardrobe, Narnia

w = Wardrobe("wood", "billy")
n = Narnia(0, "kees", w)
while not n.visit():
    n.visit()
    print("________")
