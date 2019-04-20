from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Category, LocalCategory, Types, Product

def category_list(request):
    category = Category.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'product/category_list.html', context)

def category_detail(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    # category = Category.objects.get(slug=slug)
    local = LocalCategory.objects.filter(category=category)
    context = {
        'category':category,
        'local':local
    }
    return render(request, 'product/category_detail.html', context)


def local_category_detail(request, local_slug=None, slug=None):
    local_category = get_object_or_404(LocalCategory, slug=local_slug)
    category = get_object_or_404(Category, slug=slug)
    # category = Category.objects.get(slug=slug)
    category_types = Types.objects.filter(category=local_category)
    context = {
        'category':category,
        'local_category':local_category,
        'category_types':category_types
    }
    return render(request, 'product/local_category_detail.html', context)

def local_types(request, slug=None, local_slug=None, local_type=None):
    category = get_object_or_404(Category, slug=slug)
    local_category = get_object_or_404(LocalCategory, slug=local_slug)
    locals_type = get_object_or_404(Types, slug=local_type)

    products = Product.objects.filter(category=locals_type)

    context = {
        'category':category,
        'local_category':local_category,
        'locals_type':locals_type,
        'products':products,
        }
    return render(request, 'product/local_types.html', context)

def product_detail(request, slug=None, local_slug=None, local_type=None, product_slug=None):
    category = get_object_or_404(Category, slug=slug)
    local_category = get_object_or_404(LocalCategory, slug=local_slug)
    locals_type = get_object_or_404(Types, slug=local_type)
    local_product = get_object_or_404(Product, slug=product_slug)

    context = {
        'category':category,
        'local_category':local_category,
        'locals_type':locals_type,
        'local_product':local_product
        }
    return render(request, 'product/product_detail.html', context)
