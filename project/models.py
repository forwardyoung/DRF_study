from django.db import models
from django.conf import settings
# Create your models here.

class Participation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.TextField() # 위치
    closed = models.BooleanField(default=False) # 모집 종료 여부

