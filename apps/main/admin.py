from django.contrib import admin

from django.contrib import admin

from .models import Post, Comment

# Register your models here.
admin.site.register(Post) # Це потрібно для відображення моделі в адмінці

admin.site.register(Comment) # Це потрібно для відображення моделі в адмінці
