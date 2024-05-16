from django.urls import path

from . import views
from .viewsets import QuestionListView

app_name = "polls"
urlpatterns = [
    path("list-questions/", QuestionListView.as_view({"get": "list", "post": "create"})),
    path("delete-question/<int:question_id>/", QuestionListView.as_view({"delete": "delete"})),
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

