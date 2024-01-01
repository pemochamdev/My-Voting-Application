from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    description = models.TextField()
    total_vote = models.IntegerField(default = 0)
    voters = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    


class CategoryItem(models.Model):
    
    title = models.CharField(max_length = 100)
    total_vote = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='category')
    voters = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



    def __str__(self):
        return self.title
    