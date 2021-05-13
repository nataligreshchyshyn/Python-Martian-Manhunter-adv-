class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping...')

    def study(self):
        print(f'{self.name} is studying hard')

    def work(self):
        print(f'{self.name} is earning money')


class Horse:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating grass')

    def sleep(self):
        print(f'{self.name} is sleeping while standing')

    def walk(self):
        print(f'{self.name}: "Why don\'t I break into a furious gallop?"')


class Centaur(Human, Horse):
    def __init__(self, name, sex):
        self.sex = sex
        super().__init__(name)

    def arch(self):
        if self.sex == 'male':
            print(f'{self.name} is checking the arch and preparing to war')
        else:
            print(f'{self.name} is making arrows')


if __name__ == '__main__':
    firenze = Centaur('Firenze', 'male')
    firenze.eat()
    firenze.sleep()
    firenze.study()
    firenze.work()
    firenze.walk()
    firenze.arch()
