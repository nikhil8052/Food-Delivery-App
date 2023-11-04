from django.db import models
from base.models import BaseModel
from autoslug import AutoSlugField


class Category(BaseModel):
    name=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, default=None, null=True)

class Dish(BaseModel):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True, default=None, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="dish_category")
    image=models.ImageField(upload_to="dishes")