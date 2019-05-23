from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from .models import Choice, Question
from django.contrib import auth
admin.site.register(Choice)
admin.site.unregister(auth.models.Group)
admin.site.site_header = 'Movie Voting System'

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)