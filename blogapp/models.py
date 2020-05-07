from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#from ckeditor.fields import RichTextField
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args={str(self.id)})
    
    