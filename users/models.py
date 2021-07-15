from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    OPENED_CHOICES = (
        ('OPEN', '공개'), ('NOT_OPEN', '비공개')
    )
    is_opened = models.CharField(
        max_length=10, choices=OPENED_CHOICES, default='OPEN', null=True)
