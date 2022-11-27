import random

import factory
from factory.django import DjangoModelFactory

from apps.users.models import User


class AdminUserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'admin')

    is_superuser = True
    is_staff = True
    is_active = True
    
    
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    email = 'user@user.com'
    username = 'user'
    password = factory.PostGenerationMethodCall('set_password', 'user')

    is_superuser = False
    is_staff = False
    is_active = True