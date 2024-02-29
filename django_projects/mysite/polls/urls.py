from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/<QUESTION_ID>
    path("<int:question_id>/", views.detail, name="detail"),
    # /polls/<QUESTION_ID>/results
    path("<int:question_id>/results", views.results, name="results"),
    # /polls/<QUESTION_ID/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]
