from django.db import models

# Create your models here.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title