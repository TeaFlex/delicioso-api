from django.urls import path, include
from api.utils.urls_utils import include_url_file

urlpatterns = [
    # Misc
    path("", include_url_file('misc')),

    # User
    path("user/", include_url_file('user'))
]
