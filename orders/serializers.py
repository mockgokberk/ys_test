from django.contrib.auth.models import User, Group
from rest_framework import serializers
from orders.models import Order


class SendOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id","user","address","order","quantity","status"]




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","address","order","quantity","status"]

    def to_internal_value(self, data):
        validated = {
            "id": data.get('id'),
            'user_id': data.get('user'),
            'address': data.get('address'),
            'order_id': data.get('order'),
            'quantity': data.get('quantity'),
            'status': "processed",
        }
        return validated


class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","address","order","quantity","status","created_at"]


