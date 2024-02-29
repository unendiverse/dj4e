from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/<QUESTION_ID>
    path("<int:question_id>/", views.detail, name="detail"),
    # /polls/<QUESTION_ID>/results
    path("<int:question_id>/results", views.results, name="results"),
    # /polls/<QUESTION_ID/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
    # for the autograder
    path("owner", views.owner, name="owner")
]
