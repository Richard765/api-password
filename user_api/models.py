from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.username
