from django.db import models

class Course(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title