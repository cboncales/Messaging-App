from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(max_length=100, default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']