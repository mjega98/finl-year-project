from django.db import models


class Subscribtion(models.Model):
    email = models.EmailField(unique=True)

    def __Str__(self):
        return f"{self.email}".lower()
