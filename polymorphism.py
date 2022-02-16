class Bulbasaur():
    def type(self):
      print("Leaf")

class Espeon():
    def type(self):
      print("Psychic")

def func(obj):
  obj.type()

obj_bulbasaur = Bulbasaur()
obj_espeon = Espeon()
func(obj_bulbasaur)
func(obj_espeon)
        print("Your Leafeon wandered away into the forest, chasing a butterfly. Don't worry, it always comes back.")

leafeon1 = Leafeon("Ash")
