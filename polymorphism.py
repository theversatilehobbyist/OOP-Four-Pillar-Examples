class LeafType:
    def __init__(self, trainer):
        self.trainer = trainer

    def control_over_plants(self):
        print("The Pokemon helped the flower grow!")

    def fight(self):
        print("Your Pokemon attacked the other Pokemon, the opponent lost 50 XP")

    def defend(self):
        print("Your Pokemon defended itself successfully from the other Pokemon.")

    def sleep(self):
        print("After a long day of fighting, your Pokemon went to sleep")

leaftype1 = LeafType("Ash")

class Bulbasaur(LeafType):
    def fight(self):
        print("Your Bulbasaur used its secret ability, Chlorophyll, to attack the other Pokemon, the opponent lost 75 XP")

    def defend(self):
        print("Your Bulbasaur whacked the opponent with its bulb and lashed with its vines")

    def sleep(self):
        print("Your Bulbasaur goes to sleep, dreaming of huge raspberries the size of its head")
bulbasaur1 = Bulbasaur("Ash")


class Leafeon(LeafType):
    def sleep(self):
        print("Your Leafeon went to sleep with Glaceon after a long day of fighting.")

    def chase(self):
        print("Your Leafeon wandered away into the forest, chasing a butterfly. Don't worry, it always comes back.")

leafeon1 = Leafeon("Ash")
