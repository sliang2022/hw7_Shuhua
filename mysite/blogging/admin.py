# blogging/admin.py

from django.contrib import admin
from blogging.models import Post, Category  # <-- import Category


#admin.site.register(Post)
#admin.site.register(Category)               # <-- Register Category


@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    exclude = ("posts",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
    