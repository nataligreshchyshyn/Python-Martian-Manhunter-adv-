from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, size, keyboard_model, touchpad_type, webcam_type, ports_count, dynamic_type):
        self.size = size
        self.keyboard_model = keyboard_model
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.ports_count = ports_count
        self.dynamic_type = dynamic_type

    def screen(self):
        print(f'Screen size: {self.size}')

    def keyboard(self):
        print(f'Keyboard: {self.keyboard_model}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'Webcam: {self.webcam_type}')

    def ports(self):
        print(f'Ports: {self.ports_count}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamic_type}')


if __name__ == '__main__':
    sample_laptop = HPLaptop('14"', '2UN30AA', 'Synaptics PS/2 port TouchPad', 'HP Wide Vision 720p', '5', 'B&O PLAY')
    sample_laptop.screen()
    sample_laptop.keyboard()
    sample_laptop.touchpad()
    sample_laptop.webcam()
    sample_laptop.ports()
    sample_laptop.dynamics()
