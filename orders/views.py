from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.serializers import SendOrderSerializer, OrderSerializer, ListOrderSerializer
from ystest.redis import RedisClient
from rest_framework import viewsets
from orders.models import Order
from django_filters.rest_framework import DjangoFilterBackend

class SendOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SendOrderSerializer
    queryset = Order.objects.none()

    def create(self, request, format=None):
        serializer = SendOrderSerializer(data=request.data)
        if serializer.is_valid():
            RedisClient().publish_data_on_redis(serializer.data, "orders")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = ListOrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status',)


    def list(self, request, format=None):
        serializer = ListOrderSerializer(self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, format=None):
        serializer = ListOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
