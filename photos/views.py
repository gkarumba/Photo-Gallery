# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.

def index(request):
    
    images=Image.objects.all()
    return render(request,'home.html',{"images":images})

def search_by_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        found_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"images":searched_images})
    else:
        message="No searched category"
        return render(request,'search.html',{"message":message})