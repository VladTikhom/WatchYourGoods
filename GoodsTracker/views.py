from django.shortcuts import render
from django.views.generic.base import View

from .models import Product

class ProductViewer(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'GoodsTracker/product_list.html', {'product_list': products})
