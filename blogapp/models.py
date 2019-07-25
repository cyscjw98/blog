from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title

