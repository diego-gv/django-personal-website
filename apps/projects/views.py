from django.shortcuts import render
from apps.projects.models import Project


# Create your views here.
def project_index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)


def project_details(request, _id):
    project = Project.objects.get(id=_id)

    context = {
        'project': project
    }

    return render(request, 'project_details.html', context)
