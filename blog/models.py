from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article/', blank=True)
    post = RichTextField(blank=True, null=True)


    def __str__(self):
        return self.title
    
