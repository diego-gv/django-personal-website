import random

import factory
from factory.django import DjangoModelFactory

from apps.users.models import User


class AdminUserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    email = 'admin@example.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'admin')

    is_superuser = True
    is_staff = True
    is_active = True
    
    
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    email = 'user@example.com'
    username = 'user'
    password = factory.PostGenerationMethodCall('set_password', '0000')

    is_superuser = False
    is_staff = False
    is_active = True