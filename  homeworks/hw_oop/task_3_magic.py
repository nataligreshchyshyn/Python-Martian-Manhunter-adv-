class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f'{self.name}, {self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, ' \
               f'{self.age}, {self.sex}'


if __name__ == '__main__':
    sample_obj = Profile('Barry', 'Allen', '+911911911911', 'Central City', 'b_allen@flash.com', '04.07.1986', '35', 'male')
    print(sample_obj)
