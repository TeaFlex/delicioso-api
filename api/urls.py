from django.urls import path, include
from rest_framework import routers
from api.views.Auth import AuthView
from api.views.Booking import BookingViewSet
from api.views.DinnerTable import DinnerTableViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.User import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('table', DinnerTableViewSet, basename='table')
router.register('booking', BookingViewSet, basename='booking')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    # Misc
    path("", include('api.views.misc.urls')),

    # Router
    path("", include(router.urls)),

    # Auth JWT
    path('token/', AuthView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
