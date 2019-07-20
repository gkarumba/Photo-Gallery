# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location,Category,Image
import datetime as dt
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.Nairobi= Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Travel= Category(category='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.Travel,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Category(category=list('Travel'))
        self.test_category.save_category()

        self.location = Location(location="Nairobi")
        self.location.save_location()

        self.image = Image(id=1,image_name="TopBar",category=self.test_category,location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()