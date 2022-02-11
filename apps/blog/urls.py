from django.urls import path

from apps.blog import views

urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('<int:_id>/', views.blog_details, name="blog_details"),
    path('<category>/', views.blog_category, name="blog_category")
]
