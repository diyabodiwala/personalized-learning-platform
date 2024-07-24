from django.db import models
from django.conf import settings

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
