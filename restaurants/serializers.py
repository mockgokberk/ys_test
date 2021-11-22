from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restaurants.models import Restaurant, Category, Products

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'