from django.urls import path
from .views import *

urlpatterns = [
    path('', github_login_test),
]