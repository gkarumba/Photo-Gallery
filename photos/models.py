# -*- coding: utf-8 -*-
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
    def save_location(self):
        self.save()
        
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
    
class Image(models.Model):
    image_name = models.CharField(max_length =60)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'articles/')
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image
    
    # @classmethod
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news
    
    @classmethod
    def search_by_location(cls,search_term):
        image = cls.objects.filter(location__icontains=search_term)
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image
