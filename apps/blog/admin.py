from django.contrib import admin

from apps.blog.models import Category, Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified', 'get_categories',)

    @staticmethod
    def get_categories(obj):
        categories = [c.name for c in obj.categories.all()]
        categories.sort()
        return ", ".join(categories)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
