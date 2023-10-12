# Define Hero Class
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            print("Hero is alive")
            print(
                "You (the hero) have %d health and %d power."
                % (hero.health, hero.power)
            )
            return hero.health
            # print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
            # print()
            # print("What do you want to do?")
            # print("1. fight goblin")
            # print("2. do nothing")
            # print("3. flee")
            # print(
            #     "> ",
            # )
            # user_input = input()
            # if user_input == "1":

    def attack(self, enemy):
        enemy.health -= self.power
        print("You (the hero) do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")


# Define Goblin Class
class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        print("Goblin is alive")
        print("Goblin has %d health and %d power." % (goblin.health, goblin.power))
        return goblin.health

    def attack(self, hero):
        hero.health -= self.power
        print("Goblin did %d damage to you (the hero)." % self.power)
        if hero.health <= 0:
            print("The hero is dead.")


# Instantiate goblin and hero
goblin = Goblin(6, 2)
hero = Hero(10, 5)


# hero.alive()
# goblin.alive()


while goblin.alive() and hero.alive():
    print("Hello")

#     print("You have %d health and %d power." % (hero.health, hero.power))
#     print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
#     print()
#     print("What do you want to do?")
#     print("1. fight goblin")
#     print("2. do nothing")
#     print("3. flee")
#     print(
#         "> ",
#     )
# user_input


# print(goblin.health)

# while Goblin.alive() and Hero.alive():
#     print("You have %d health and %d power." % (Hero.health, Hero.power))
#     print("The goblin has %d health and %d power." % (Goblin.health, Goblin.power))
#     print()
#     print("What do you want to do?")
#     print("1. fight goblin")
#     print("2. do nothing")
#     print("3. flee")
#     print(
#         "> ",
#     )
#     user_input = input()
