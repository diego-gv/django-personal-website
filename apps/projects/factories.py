import random

import factory
from factory.django import DjangoModelFactory

from apps.projects.models import Project


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.Faker("sentence", nb_words=2, variable_nb_words=True)
    description = factory.Faker("sentence", nb_words=10, variable_nb_words=True)
    technology = factory.Faker("sentence", nb_words=1, variable_nb_words=True)
    image = random.choice(['img/django_logo.png', 'img/flask_logo.png'])

