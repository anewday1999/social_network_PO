from django.test import TestCase
from profiles.models import User
from datetime import date

class UserTestCase(TestCase):
    def setUp(self):
        cur_date = date(2022, 5, 30)
        self.arg = {
            'full_name': "Test full_name",
            'email': "testmail@gmail.com",
            'address': 'Test address',
            'school': 'Test school',
            'specialize': 'Test specialize',
            'yearofschool': 10,
            'sexs': 'Male',
            'years_of_birth': 15,
            'more': 'More about user',
            'paid_until': cur_date,
            'is_sub_findtutor': True,
            'is_sub_market': False, 
            'is_sub_employee': False,
            'is_sub_homework': False,
            'is_verified': False,
        }
        self.user = User(
            full_name = self.arg['full_name'],
            email = self.arg['email'],
            address = self.arg['address'],
            school = self.arg['school'],
            specialize = self.arg['specialize'],
            yearofschool = self.arg['yearofschool'],
            sexs = self.arg['sexs'],
            years_of_birth = self.arg['years_of_birth'],
            more = self.arg['more'],
            paid_until = self.arg['paid_until'],
            is_sub_findtutor = self.arg['is_sub_findtutor'],
            is_sub_market = self.arg['is_sub_market'],
            is_sub_employee = self.arg['is_sub_employee'],
            is_sub_homework = self.arg['is_sub_homework'],
            is_verified = self.arg['is_verified'],
        )
    
    def compare_with(self, res, user=None):
        if user == None:
            user = self.user
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.full_name, res['full_name'])
        self.assertEqual(user.email, res['email'])
        self.assertEqual(user.address, res['address'])
        self.assertEqual(user.school, res['school'])
        self.assertEqual(user.specialize, res['specialize'])
        self.assertEqual(user.yearofschool, res['yearofschool'])
        self.assertEqual(user.sexs, res['sexs'])
        self.assertEqual(user.years_of_birth, res['years_of_birth'])
        self.assertEqual(user.more, res['more'])
        self.assertEqual(user.paid_until, res['paid_until'])
        self.assertEqual(user.is_sub_findtutor, res['is_sub_findtutor'])
        self.assertEqual(user.is_sub_market, res['is_sub_market'])
        self.assertEqual(user.is_sub_employee, res['is_sub_employee'])
        self.assertEqual(user.is_sub_homework, res['is_sub_homework'])
        self.assertEqual(user.is_verified, res['is_verified'])
    
    def test_User(self):
        res = self.arg.copy()
        self.compare_with(res)

