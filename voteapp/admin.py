from django.contrib import admin

# Register your models here.

from voteapp.models import Category, CategoryItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_vote', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':("title", )}


@admin.register(CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_vote', 'category', 'created_at', 'updated_at']
    
