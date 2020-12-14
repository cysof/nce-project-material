from django.urls import path
from . import views
from .views import (ProjectListView, ProjectDetailView)

app_name = 'nce'
urlpatterns = [
    path("", ProjectListView.as_view(), name="index_view"),
    path("<int:id>/", ProjectDetailView.as_view(), name="ProjectDetailView"),
    path("<departments>/", views.departments, name="departments"),
]
