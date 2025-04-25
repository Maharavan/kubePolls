from django.contrib import admin
from .models import VoteQuestions, Choices
# Register your models here.
admin.site.register(VoteQuestions)
admin.site.register(Choices)