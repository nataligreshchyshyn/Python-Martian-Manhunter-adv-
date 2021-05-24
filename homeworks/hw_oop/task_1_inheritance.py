class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eating...')

    def sleep(self):
        print(f'{self.name} sleeping... ZZZ')


class Cat(Animals):
    def hunt_mice(self, amount):
        if amount == 0:
            print(f'{self.name} is a bad hunter')
        elif amount == 1:
            print(f'{self.name} has caught a mouse')
        else:
            print(f'{self.name} has just caught {amount} mice')


class Fish(Animals):
    def swim(self):
        print(f'{self.name} is swimming in the aquarium')


class Spider(Animals):
    def bite(self):
        print(f'{self.name} is biting Peter Parker')


class Mayfly(Animals):
    def talk(self):
        print(f'{self.name}: "This is the last day of my life..."')


class Sloth(Animals):
    def work(self):
        print(f'{self.name} still hasn\'t started')


if __name__ == '__main__':
    nick = Cat('Nick')
    ariel = Fish('Ariel')
    webster = Spider('Webster')
    zipper = Mayfly('Zipper')
    flash = Sloth('Flash')

    nick.hunt_mice(1)
    ariel.swim()
    webster.bite()
    zipper.talk()
    flash.work()

    for pet in (nick, ariel, webster, zipper, flash):
        print(f'{pet.name} is the one of Animals:', isinstance(pet, Animals))
