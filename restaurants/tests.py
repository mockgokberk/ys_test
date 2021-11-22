from django.test import TestCase
from .models import Restaurant, Products, Category
# Create your tests here.

class RestaurantTestCase(TestCase):

    def setUp(self):
        r = Restaurant(name="Büfe")
        r.save()
        c = Category(name="Fast Food")
        c.save()
        p = Products(name="Hamburger", category=c, restaurants=r)
        p.save()

    def test_get_restauran(self):
        r = Restaurant.objects.get(name="Büfe")
        self.assertEqual(r.name,"Büfe")

    def test_get_category(self):
        c = Category.objects.get(name="Fast Food")
        self.assertEqual(c.name,"Fast Food")

    def test_get_product(self):
        p = Products.objects.get(name="Hamburger")
        self.assertEqual(p.name,"Hamburger")

