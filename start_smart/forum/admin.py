from django.contrib import admin
from .models import UserProfileInfo,forum_text,Comment
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(forum_text)
admin.site.register(Comment)
