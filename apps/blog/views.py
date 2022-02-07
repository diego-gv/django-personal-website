from django.shortcuts import render

from apps.blog.forms import CommentForm
from apps.blog.models import Post, Comment


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts
    }

    return render(request, 'blog_index.html', context)


def blog_details(request, _id):
    post = Post.objects.get(id=_id)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "blog_details.html", context)


def blog_category(request, category):
    posts = Post.objects.all().filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts
    }

    return render(request, 'blog_category.html', context)
