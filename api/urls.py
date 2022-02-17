from django.urls import path
from .views.misc.Misc import MiscView

urlpatterns = [
    path(MiscView.get_prefix(), MiscView.as_view()),
]
