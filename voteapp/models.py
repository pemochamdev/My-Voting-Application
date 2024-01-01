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


    @property
    def percentage_vote(self):
        category_vote = self.category.total_vote
        category_item_vote = self.total_vote
        if category_vote == 0:
            vote_in_percentage = 0
        else:
            vote_in_percentage = (category_item_vote/category_vote)*100
        
        return vote_in_percentage


    def __str__(self):
        return self.title
    