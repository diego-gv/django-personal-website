from django.contrib import admin

from apps.blog.models import Category, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified', 'get_categories',)

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
