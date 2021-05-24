class CellPhone:
    def __init__(self, screen, case):
        self.screen = screen
        self.case = case


class Screen:
    def __init__(self, size):
        self.size = size


class Case:
    def __init__(self, color):
        self.color = color


if __name__ == '__main__':
    sample_screen = Screen('4.7"')
    sample_case = Case('red')
    sample_phone = CellPhone(sample_screen, sample_case)
    print(sample_phone.case.color, sample_phone.screen.size)
