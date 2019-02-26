from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    #return HttpResponse('Epa bro!')
    objects = Product.objects.all()
    context = {
       'products'  : objects
    }
    return render(request, 'index.html', context)



def add_product(request):
    return HttpResponse('Add a product!')

