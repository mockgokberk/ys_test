from django.test import TestCase
from restaurants.models import Restaurant, Products, Category
from orders.models import Order
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ystest.redis import RedisClient
import redis

class OrdersTestCase(TestCase):

    def setUp(self):
        r = Restaurant(name="Büfe")
        r.save()
        c = Category(name="Fast Food")
        c.save()
        p = Products(name="Hamburger", category=c, restaurants=r)
        p.save()
        u = User(username="testuser")
        u.save()

    def test_create_order(self):
        o = Order(user_id=1, address="testadress",
                  order=Products(name="Hamburger", restaurants_id=1))
        self.assertEqual(o.address, "testadress")


class OrdersApiTestCase(TestCase):

    def setUp(self):
        self.factory = APIClient()
        r = Restaurant(name="Büfe")
        r.save()
        self.r = Restaurant.objects.get(name="Büfe")
        c = Category(name="Fast Food")
        c.save()
        self.c = Category.objects.get(name="Fast Food")
        p = Products(name="Hamburger", category=c, restaurants=r)
        p.save()
        self.p = Products.objects.get(name="Hamburger")
        u = User(username="testuser")
        u.save()
        self.u = User.objects.get(username="testuser")

    def test_order_create(self):
        r = self.factory.post('/api/v1/create_order/', {
            "user": self.u.id,
            "address": "testadress",
            "order": self.p.id,
            "quantity": "1",
            "status": "preparing"
        }, format='json')
        self.assertEqual(r.status_code, 201)

    def test_order_process(self):
        r = self.factory.post('/api/v1/order/', {
            "user": self.u.id,
            "address": "testadress",
            "order": self.p.id,
            "quantity": "1",
            "status": "preparing"
        }, format='json')

        self.assertEqual(r.status_code, 201)

    def test_order_get(self):
        r = self.factory.get('/api/v1/order/', format='json')
        self.assertEqual(r.status_code, 200)
class RedisTestCase(TestCase):
    def test_redis(self):
        con = RedisClient().get_client()
        self.assertIsInstance(con,redis.client.Redis)