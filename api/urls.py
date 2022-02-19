from django.urls import path, include
from rest_framework import routers

from api.views.tables.Tables import TableViewSet

router = routers.SimpleRouter()

router.register('tables', TableViewSet, basename='tables')

urlpatterns = [
    # Misc
    path("", include('api.views.misc.urls')),

    # Auth
    path("auth/", include('rest_framework.urls')),

    # Router
    path("", include(router.urls)),
]
