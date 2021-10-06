from django.urls import path
from .views import HomePageView, PostView , MainPageView


app_name='appone'

urlpatterns = [
    path('home/', HomePageView.as_view() , name="index"),
    path('post/', PostView.as_view(), name="post"),
    path('', MainPageView.as_view(), name="mainpage"),
]