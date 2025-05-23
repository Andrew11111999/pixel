from django.db import models

class StaticContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static_content/', null=True, blank=True)

    def __str__(self):
        return self.title
