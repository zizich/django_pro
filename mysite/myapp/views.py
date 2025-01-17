from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
  items = Product.objects.all()

  context = {
    "items": items
  }
  return render(request, 'myapp/index.html', context)

def indexItem(request, id):
  items = Product.objects.get(id=id)

  context = {
    "items": items
  }

  return render(request, 'myapp/detail.html', context)
