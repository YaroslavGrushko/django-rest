from django.db import models

# Create your models here.

class TestExample(models.Model):
    nickname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nickname} {self.country}"
