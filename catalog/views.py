from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Category, Product


# def index(request):
#     page_title = 'Music instruments and sheet music for musicians'
#     products = Product.objects.filter(is_active=True)

#     template_name = 'home.html'
#     context = {
#         'user': request.user,
#         'products': products
#     }

#     return render(request, template_name, context)

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()
    print(category)
    template_name = 'catalog/category.html'
    context = {
        'category': category,
        'products': products,
    }

    return render(request, template_name, context)

def show_products(request):
    products = Product.objects.filter(is_active=True)

    template_name = 'catalog/products.html'
    context = {
        'products': products,

    }

    return render(request, template_name, context)


def show_product_detail(request, slug):
    # Get a single product from the database based on the slug
    product = get_object_or_404(Product, slug=slug)

    template_name = 'catalog/detail.html'

    context = {
        'product': product
    }

    return render(request, template_name, context)