import random

from django.core.management import BaseCommand
from django.db import transaction

from apps.blog.factories import CategoryFactory, CommentFactory, PostFactory
from apps.blog.models import Category, Comment, Post

N_CATEGORIES = 5
N_POSTS = 5
N_CATEGORIES_BY_POST = 2
N_COMMENTS_BY_POST = 25


class Command(BaseCommand):
    help = "This command generate a dummy data for simulate complete use"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Category, Post, Comment]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        categories = []
        for i in range(N_CATEGORIES):
            categories.append(CategoryFactory())

        for _ in range(N_POSTS):
            post_categories = random.choices(categories, k=N_CATEGORIES_BY_POST)
            post = PostFactory(categories=post_categories)
            random_n_comments = random.randint(0, N_COMMENTS_BY_POST)
            for _ in range(random_n_comments):
                CommentFactory(post=post)
