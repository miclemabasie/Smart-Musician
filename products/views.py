from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product

def product_list_view(request):
    page_title = 'Product_listing'
    template_name = 'products/catalog.html'
    context = {
        'user': 'miclem',
        'page_title': page_title,
        'products': ['product1', 'product2', 'product3', 'product4']
    }

    # return HttpResponse("<h1>This is just a hello world program </h1>")
    return render(request, template_name, context)










    