import unittest
from employee import Employee
from unittest.mock import patch


class TestForEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee('Barry', 'Allen', 10000)

    def test_employee_raise(self):
        self.assertTrue(self.classTest.pay < int(self.classTest.pay * Employee.raise_amt))
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 10500)

    def test_email_property(self):
        self.assertEqual(self.classTest.email, f'Barry.Allen@email.com')

    def test_fullname_property(self):
        self.assertEqual(self.classTest.fullname, f'Barry Allen')

    @patch('requests.get')
    def test_monthly_schedule(self, mock_request):
        mock_request.return_value.ok = True
        response = f'{self.classTest.last}\'s schedule for month'
        mock_request.return_value.text = response
        self.assertEqual(self.classTest.monthly_schedule('may'), response)
        mock_request.return_value.ok = False
        self.assertEqual(self.classTest.monthly_schedule('may'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
