from django.db import models
from django.contrib.auth.models import User


# Blog model.
class BlogModel(models.Model):
    blog_title = models.CharField(max_length=50, default='')
    blog_entry = models.TextField(default='')
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.blog_title
