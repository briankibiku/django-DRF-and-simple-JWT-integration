from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
"""
class Post:
    id int
    titile str(50)
    content text
    created datetime
"""

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
