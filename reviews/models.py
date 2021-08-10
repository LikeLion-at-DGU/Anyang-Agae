from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    hospital = models.CharField(max_length=100, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:10]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)