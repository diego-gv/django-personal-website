from django.contrib import admin

from apps.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', )
    exclude = ('image', )  # TODO: hay que conseguir que sea modificable a través del panel de administración


# Register your models here.
admin.site.register(Project, ProjectAdmin)
