from django.contrib import admin

# Register your models here.
from .models import Question


# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
        list_display=['category',]