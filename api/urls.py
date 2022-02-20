from django.urls import path, include
from rest_framework import routers
from api.views.Booking import BookingViewSet
from api.views.DinnerTable import DinnerTableViewSet

router = routers.SimpleRouter()

router.register('table', DinnerTableViewSet, basename='table')
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = [
    # Misc
    path("", include('api.views.misc.urls')),

    # Router
    path("", include(router.urls)),
]
