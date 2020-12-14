from django.shortcuts import render, get_object_or_404
from nce.models import Department, Project
from django.views.generic import (
    ListView, DetailView)

# Create your views here.

from .models import Project


class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'index.html'


def departments(request, department):
    projects = Project.objects.filter(
        departments__name__contains=department
    )
    context = {
        'department': department,
        'projects': projects
    }
    return render(request, "departments.html", context)


class ProjectDetailView(DetailView):
    template_name = 'project_view.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Project, id=id_)

