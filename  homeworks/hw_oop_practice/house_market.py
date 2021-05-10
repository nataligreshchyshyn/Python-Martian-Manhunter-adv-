from abc import ABC, abstractmethod


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses=None, discount=True):
        self.name = name
        self.discount = discount
        self.houses = houses
        self._transaction_history = []

    def add_transaction(self, person):
        self._transaction_history.append(person)
        return True

    def provide_info(self, person):
        print(f'Welcome, {person.name}! My name is {self.name}\n'
              f'Let me present you all our available houses:\n')
        for x in self.houses:
            print(f'{x.name} with an area of {x.area} sq.m costs ${x.cost}\n')

    def give_discount(self, person):
        if self.discount and len(self._transaction_history) % 9 == 0:
            print(f'{person.name}, you are so lucky! You have just got a 10% discount!')
            return True
        else:
            return False

    def steal_money(self, person, house_price):
        if len(self._transaction_history) % 10 == 0:
            person.money -= house_price
            return True

    def sell_house(self, person, house):
        try:
            self.add_transaction(person)
            if self.steal_money(person, house.cost):
                print(f'{person.name}, thank you for such a generous donation. God bless you! Bye!\n'
                      f'{self.name} is running...')
                return False
            else:
                person.money -= house.cost - house.cost * 0.1 if self.give_discount(person) else house.cost
                self.houses.remove(house)
                return True
        except ValueError:
            self._transaction_history.remove(person)
            print(f'Sorry, seems like {house.name} is not available anymore\n'
                  f'{person.name}, please ask {self.name} to provide an information about available houses first')


class Person(ABC):
    def __init__(self, name, age, money, own_house):
        self.name = name
        self.age = age
        self.money = money
        self.own_house = own_house

    def check_house_cost(self, house):
        if self.money >= house.cost:
            return True
        else:
            return False

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, realtor, house):
        raise NotImplementedError


class Human(Person):
    def __init__(self, name, age, money, own_house=False):
        super().__init__(name, age, money, own_house)

    def info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old.\n'
              f'I have ${self.money} to spend')

    def make_money(self):
        self.money += 10000
        print(f'{self.name} has just got $10000')

    def buy_house(self, realtor, house):
        if self.check_house_cost(house):
            if realtor.sell_house(self, house):
                if self.own_house:
                    print(f'{self.name} has just bought another house')
                else:
                    self.own_house = True
                    print(f'{self.name} has just bought their first house')
            else:
                print(f'{self.name}, please check your money and let\'s proceed')
        else:
            print(f'Sorry, {self.name}, you can\'t afford this house.\n'
                  f'Work harder!\n'
                  f'You should probably think about a career in IT ;)')


class House:
    def __init__(self, name, cost, area):
        self.name, self.area, self.cost = name, area, cost


class SmallTypicalHouse(House):
    def __init__(self, name, cost, area=40):
        super().__init__(name, cost, area)


villa = House('villa', 60000, 100)
dacha = House('dacha', 120000)
castle = House('castle', 1000000000, 500)
castle_1 = House('castle_1', 200000, 100)
barak = House('barak', 300000)
sm = SmallTypicalHouse('sm', 20000)
sm_1 = SmallTypicalHouse('sm_1', 20000)
sm_2 = SmallTypicalHouse('sm_2', 20000)
sm_3 = SmallTypicalHouse('sm_3', 20000)
sm_4 = SmallTypicalHouse('sm_4', 20000)
sm_5 = SmallTypicalHouse('sm_5', 20000)
sm_6 = SmallTypicalHouse('sm_6', 20000)
sm_7 = SmallTypicalHouse('sm_7', 20000)

nata = Human('Nata', 31, 70000)
yurii = Human('Yurii', 33, 120000)
sirko = Human('Sirko', 23, 200000)
nik = Human('Nick', 18, 200000)
bil = Human('Bil', 25, 1000000000)
ksu = Human('Oksana', 40, 2000000000, True)
frodo = Human('Frodo', 28, 800000)
sam = Human('Sam', 28, 800000)
alex = Human('Alex', 28, 800000)
anna = Human('Anna', 28, 800000)
ariel = Human('Ariel', 28, 800000)

adolf = Realtor('Adolf', houses=[villa, dacha, castle, castle_1, barak, sm, sm_1, sm_2, sm_3, sm_4, sm_5, sm_6, sm_7])

adolf.provide_info(ksu)
ksu.buy_house(adolf, villa)
anna.buy_house(adolf, castle_1)
nata.info()
nata.buy_house(adolf, villa)
adolf.provide_info(nata)
nata.buy_house(adolf, dacha)
nata.make_money()
yurii.buy_house(adolf, sm_1)
ariel.buy_house(adolf, sm_2)
alex.buy_house(adolf, sm_3)
sam.buy_house(adolf, sm)
frodo.buy_house(adolf, sm_4)
bil.buy_house(adolf, sm_5)
nik.buy_house(adolf, sm_6)
print(f'Sirko\'s money before: {sirko.money} and home status: {sirko.own_house}')
sirko.buy_house(adolf, sm_7)
print(f'Sirko\'s money after: {sirko.money} and home status: {sirko.own_house}')

