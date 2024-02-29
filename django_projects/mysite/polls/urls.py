from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/<QUESTION_ID>
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/<QUESTION_ID>/results
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    # /polls/<QUESTION_ID/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
    # for the great and wise autograder
    path("owner", views.owner, name="owner"),
]
