from django.urls import path, include

from apps.users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name="dashboard"),
]
