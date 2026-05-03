from django.db import models
from django.conf import settings


# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
