from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):

    GRADE_CHOICES=(
        ('1','★☆☆☆☆'),
        ('2','★★☆☆☆'),
        ('3','★★★☆☆'),
        ('4','★★★★☆'),
        ('5','★★★★★'),
    )
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grade=models.CharField(max_length=5, choices=GRADE_CHOICES,null=True)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:10]