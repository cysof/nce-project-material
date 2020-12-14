from django.contrib import admin
from nce.models import Project, Department


class ProjectAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Department, DepartmentAdmin)
