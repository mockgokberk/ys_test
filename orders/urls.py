from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'create_order', views.SendOrderViewSet, basename="send_order")
router.register(r'order', views.OrderViewSet, basename="order")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls))
]