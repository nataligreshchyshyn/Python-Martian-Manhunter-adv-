class Person:
    def __init__(self):
        head = Head('This is my face')
        body = Body('This is a slim body')
        left_hand = Hand('This is a left hand')
        right_hand = Hand('This is a right hand')
        left_leg = Leg('This is a left leg')
        right_leg = Leg('This is a right leg')
        self.human_parts = [head, body, left_hand, right_hand, left_leg, right_leg]


class Head:
    def __init__(self, char):
        self.char = char


class Body:
    def __init__(self, char):
        self.char = char


class Hand:
    def __init__(self, char):
        self.char = char


class Leg:
    def __init__(self, char):
        self.char = char


if __name__ == '__main__':
    sample_person = Person()
    for part in sample_person.human_parts:
        print(part.char)