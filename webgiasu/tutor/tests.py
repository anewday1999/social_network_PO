from calendar import calendar
from django.test import TestCase
from django.contrib.auth import get_user_model
from tutor.models import findtutorpost

from datetime import date

class findtutorpostTestCase(TestCase):
    def setUp(self):
        cur_date = date(2022, 4, 30)
        self.arg = { 
            "title": "Test title",
            "main_content": "Test main_content",
            "subject": "Test subject",
            "calendar": "Test calendar",
            "salary": "Test salary",
            "contact": "Test contact",
            "date_posted": cur_date,
            "date_outdate": 12
            }
        self.post = findtutorpost(
            title = self.arg["title"],
            main_content = self.arg["main_content"],
            subject = self.arg["subject"],
            calendar = self.arg['calendar'],
            salary = self.arg['salary'],
            contact = self.arg["contact"],
            date_posted = self.arg["date_posted"],
            date_outdate = self.arg["date_outdate"],
        )
    
    def compare_with(self, res, post=None):
        if (post == None):
            post = self.post
        self.assertTrue(isinstance(post, findtutorpost))
        self.assertEqual(post.title, res['title'])
        self.assertEqual(post.main_content, res['main_content'])
        self.assertEqual(post.subject, res['subject'])
        self.assertEqual(post.calendar, res['calendar'])
        self.assertEqual(post.salary, res['salary'])
        self.assertEqual(post.contact, res['contact'])
        self.assertEqual(post.date_posted, res['date_posted'])
        self.assertEqual(post.date_outdate, res['date_outdate'])
    
    def test_findtutorpost(self):
        res = self.arg.copy()
        self.compare_with(res)
# Create your tests here.
