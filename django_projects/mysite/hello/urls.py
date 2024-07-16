from django.urls import path

from . import views

app_name = "hello"
urlpatterns = [
    # /polls/
    path('', views.myview),
]