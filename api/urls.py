from django.urls import include, path
from rest_framework import routers
from orders.urls import router as order_router
from restaurants.urls import router as restaurant_router
from api import views

router = routers.DefaultRouter()
router.registry.extend(order_router.registry)
router.registry.extend(restaurant_router.registry)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]