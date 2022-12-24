import factory
from factory.django import DjangoModelFactory

from apps.blog.models import Category, Post, Comment


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("slug")


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    body = factory.Faker("sentence", nb_words=500, variable_nb_words=True)
    # categories = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.categories.add(category)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.Faker("user_name")
    body = factory.Faker("sentence", nb_words=10, variable_nb_words=True)
    post = factory.SubFactory(PostFactory)
