from django.urls import path, include

from .User import UserView
from .Auth import AuthView

urlpatterns = [
    path("<int:userid>/", UserView.as_view()),
    path("auth/", AuthView.as_view())
]
