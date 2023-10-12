# Define Character Parent Class
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            print("%s is alive" % self.name)
            print(
                "%s has %d health and %d power." % (self.name, self.health, self.power)
            )
            return self.health

    def attack(self, opposition):
        print("Attack is useless! Zombies are already undead!")
        self.print_status()
        if opposition.health <= 0:
            print("The %s is dead." % (self.name))


# Define Hero Child Class
class Hero(Character):
    def print_status(self):
        print("%s is alive" % self.name)
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        return self.health


# Define Goblin Child Class
class Goblin(Character):
    def print_status(self):
        print("%s is alive" % self.name)
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        return self.health


class Zombie:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def print_status(self):
        print("%s is alive" % self.name)
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        return self.health

    def alive(self):
        print("%s is alive, FOREVER!!" % self.name)
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        return self.health

    def attack(self, hero):
        hero.health -= self.power
        self.print_status()
        if hero.health <= 0:
            print("The %s is dead." % (hero.name))


# Instantiate goblin and hero and zombie
goblin = Goblin(6, 2, "GOBLIN--BOIIII")
hero = Hero(10, 5, "Mr. HERO")
zombie = Zombie(1, 1, "ZORGU")


while zombie.alive() and hero.alive():
    print("You have %d health and %d power." % (hero.health, hero.power))
    print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. Fight goblin")
    print("2. Do nothing")
    print("3. Flee")
    print("4. Goblin attacks you")
    print(
        "> ",
    )
    user_input = input()
    if user_input == "1":
        hero.attack(goblin)
    elif user_input == "2":
        # print("Don't be scared, come fight!")
        pass
    elif user_input == "3":
        print("Goodbye")
        break
    elif user_input == "4":
        zombie.attack(hero)
    else:
        print("Invalid input %r" % user_input)
