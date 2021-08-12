from django.contrib.auth.models import User
from django.db import models
from users.models import Profile
from django.urls import reverse


class Event(models.Model):
    start_time = models.DateTimeField("날짜")
    title = models.CharField("제목", max_length=50)
    description = models.TextField("특이사항")
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('diary:detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
