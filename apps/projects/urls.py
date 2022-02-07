from django.urls import path
from apps.projects import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:_id>/', views.project_details, name='project_details')
]
