from django.contrib import admin

from apps.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
