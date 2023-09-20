from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'type', 'time_created', 'title', 'rating')
    list_display_links = ('id', 'author')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
