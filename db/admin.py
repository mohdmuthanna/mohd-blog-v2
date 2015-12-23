from django.contrib import admin

# Register your models here.
from .models import Category, Post

class PostInline(admin.StackedInline):
    model = Post

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline,]
    # pass


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
