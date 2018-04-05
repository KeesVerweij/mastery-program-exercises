import random


class Narnia:
    def __init__(self, visits, name, wardobe):
        self.visits = visits
        self.name = name
        self.wardrobe = wardobe

    def visit(self):
        print(self.wardrobe.kick())
        print(self.wardrobe.open())
        if self.wardrobe.get_in():
            self.visits += 1
            print(self.visits)
            witch = Witch(self.visits, self.name)
            win = witch.fight()
            if win is True:
                aslan = Aslan(self.visit, self.name)
                aslan.visit()
                return True
            else:
                print(self.wardrobe.get_out())
                print(self.wardrobe.close())
                return False
        else:
            print(self.wardrobe.get_out())
            print(self.wardrobe.close())
            return False


class Aslan:
    def __init__(self, visits, name):
        self.visits = visits
        self.name = name

    def visit(self):
        print("Ah, " + self.name + " after " + str(self.visits) + " You finally meet the great Aslan!")


class Witch:
    def __init__(self, visits, name):
        self.visits = visits
        self.name = name

    def fight(self):
        if self.visits == 0:
            print("Krakrakra! Hello, your name is " + self.name + " right? Get ready to fight!!")
        else:
            print("Hello, " + self.name + " Krakrakra! We meet again for the " +
                  str(self.visits) + " time, get ready to fight!!")
        if random.randint(self.visits, 99) == 99:
            print("You have defeated me, " + self.name + "! Krakrakra!")
            print("you may visit aslan!")
            return True
        else:
            print("You have failed, " + self.name + "! Krakrakra! Better luck next time!")
            return False


class Wardrobe:
    def __init__(self, material, name, is_open=False, is_occupied=False):
        self.material = material
        self.name = name
        self.is_open = is_open
        self.is_occupied = is_occupied

    def __str__(self):
        return self.material + ", " + self.name + ", " + str(self.is_open) + ", " + str(self.is_occupied)

    def open(self):
        if self.is_open:
            return "the wardrobe is already open.."
        else:
            self.is_open = True
            return "you opened the wardobe!"

    def close(self):
        if not self.is_open:
            return "the wardrobe is already closed.."
        else:
            self.is_open = False
            return "you closed the wardobe!"

    def get_in(self):
        if not self.is_open:
            return "the door is closed, you can't get in"
        elif self.is_occupied:
            return "you are already in the closet.."
        else:
            self.is_occupied = True
            print("you got into the wardobe!")
            if random.randint(0, 99) == 10:
                print("you are in Narnia!")
                return True
            else:
                return False

    def get_out(self):
        if not self.is_occupied:
            return "you are not in the closet.."
        elif not self.is_open:
            return "the door is closed, you can't get out"
        else:
            self.is_occupied = False
            return "you got out of the wardobe!"

    def kick(self):
        # valid_materials = ["wood", "carbon", "glass"]
        # valid = [materials for materials in valid_materials if materials == self.material.lower()]
        # if not valid:
        if self.is_occupied:
            return "you don't have enough space to kick from within the closet.."
        elif self.material == "wood":
            return "'Boem!'"
        elif self.material == "carbon":
            return "'Tok!'"
        elif self.material == "glass":
            return "'Ting!'"
        else:
            return "can't kick the closet your closet is made out of a kick-resistant material!"
