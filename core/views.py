from itertools import product

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Subscribers
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, Wishlist, ProductImages, ProductReview, Address


# Create your views here.
def index(request):
    #products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products":products
    }

    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        "products": products
    }

    return render(request, 'core/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'core/category-list.html', context)

def subscribers(request):
    if request.method=="POST":
        subscriber=Subscribers()
        email=request.POST.get('email')

        subscriber.email=email
        subscriber.save()
        return HttpResponse("<h1>THANKS FOR SUBSCRIBING</h1>")
    return render(request, 'core/index.html')

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    #product = get_object_or_404(Product, pid=pid)

    context = {
        "product": product,
    }

    return render(request, "core/product-detail.html", context)
