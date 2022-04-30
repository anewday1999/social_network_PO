from django.test import TestCase
from django.contrib.auth import get_user_model
from market.models import marketpost

from datetime import date

class marketpostTestCase(TestCase):
    def setUp(self):
        cur_date = date(2022, 4, 30)
        self.arg = { 
            "title": "Test title",
            "describe": "Test descript",
            "address": "Test address",
            "contact": "Test contact",
            "price": "100",
            "date_posted": cur_date,
            "date_outdate": 12,
            }
        self.post = marketpost(
            title = self.arg["title"],
            describe = self.arg["describe"],
            address = self.arg["address"],
            contact = self.arg["contact"],
            price = self.arg["price"],
            date_posted = self.arg["date_posted"],
            date_outdate = self.arg["date_outdate"],
        )
    
    def compare_with(self, res, post=None):
        if (post == None):
            post = self.post
        self.assertTrue(isinstance(post, marketpost))
        self.assertEqual(post.title, res['title'])
        self.assertEqual(post.describe, res['describe'])
        self.assertEqual(post.address, res['address'])
        self.assertEqual(post.contact, res['contact'])
        self.assertEqual(post.price, res['price'])
        self.assertEqual(post.date_posted, res['date_posted'])
        self.assertEqual(post.date_outdate, res['date_outdate'])
    
    def test_marketpost(self):
        res = self.arg.copy()
        self.compare_with(res)

