from django.db import models

# Create your models here.
class Items(models.Model):
    text = models.CharField(max_length=40, null=False)
    complete = models.BooleanField(default=False)

    def json(self):
        return {
            'id': self.id,
            'text': self.text,
            'complete': self.complete,
        }

    class Meta:
        ordering = ['complete', 'id']
