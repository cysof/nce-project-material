from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView)
from .models import Project, Department


class ListOfDepart(ListView):
    model = Department
    template_name = 'nceprojectsite/list_of_departments.html'


class ListOfProject(ListView):
    model = Project
    template_name = 'nceprojectsite/index.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'nceprojectsite/project_detail.html'
