from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    class Meta:
        ordering = ['id']
        db_table = 'user_profile'

        verbose_name = 'user_profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    OPENED_CHOICES = (
        ('공개', '공개'), ('비공개', '비공개')
    )
    is_opened = models.CharField(
        max_length=10, choices=OPENED_CHOICES, default='공개')
