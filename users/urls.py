

from django.contrib import admin
from django.urls import path

from users.views import HomePageView,SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view() , name='signup'),
]
