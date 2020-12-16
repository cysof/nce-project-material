from django.urls import path
from . import views
from .views import (ListOfDepart, ListOfProject, ProjectDetailView)

app_name = 'nce'
urlpatterns = [
    path("", ListOfProject.as_view(), name="index_view"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("list_of_departments", ListOfProject.as_view(), name="list_of_departments"),
]
