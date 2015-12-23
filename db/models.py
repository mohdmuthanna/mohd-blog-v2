from django.db import models
from django.contrib.auth.models import User
import sys
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
         return self.name

class Post(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,)
    publish_at = models.DateTimeField(auto_now=True, editable=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    def get_excerpt(self):
        index = self.text.index('---')
        if self.category.name == 'arabic':
            read_more = "<إقرأ المزيد>"
        else:
            read_more = "<read more>"
        return self.text[:index] + read_more


    def get_excerpt_full(self):
        i = self.text.index('---')
        result = self.text[:i] + self.text[i+3:]
        return result

    # if diffrent bitween create & update more than n minutes
    # print update date
    def is_updated(self):
        delta = self.update_at - self.create_at
        if (delta.seconds/60) > 10:
            return True
        else:
            return False


    def __str__(self):
         return self.title

    @classmethod
    def get_lastest_visible(cls, category):
        try:
            return Post.objects.filter(
                is_visible=True,
                category__name=category,
            ).latest('create_at')
        except:
            return None
