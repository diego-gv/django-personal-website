import factory
from factory.django import DjangoModelFactory

from apps.blog.models import Category, Post, Comment


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('slug')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    body = factory.Faker("sentence", nb_words=500, variable_nb_words=True)
    # categories = factory.SubFactory(CategoryFactory)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.Faker('user_name')
    body = factory.Faker("sentence", nb_words=10, variable_nb_words=True)
    post = factory.SubFactory(PostFactory)

