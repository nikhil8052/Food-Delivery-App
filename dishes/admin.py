from django.contrib import admin
from .models import Dish
from .models import Category
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display=['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Dish,DishAdmin)
admin.site.register(Category,CategoryAdmin)