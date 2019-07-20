# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image,Location
# Create your views here.

def index(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'home.html',{"images":images, "location": location})

def index1(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'home1.html',{"images":images, "location": location})

def index2(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'home2.html',{"images":images, "location": location})

def search_by_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        print(search_term)
        found_images = Image.search_by_category(search_term)
        print(found_images)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"images":found_images})
    else:
        message="No searched category"
        return render(request,'search.html',{"message":message})
    
def search_by_location(request, location):
    locations = Location.objects.all()
    images = Image.search_by_location(location)
    print(images)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title': title, 'images': images, 'locations': locations})