from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class VoteQuestions(models.Model):
    question = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return f"{self.question}"

class Choices(models.Model):
    question_id = models.ForeignKey(VoteQuestions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return f"Choice: {self.choice} (Votes: {self.vote})"
