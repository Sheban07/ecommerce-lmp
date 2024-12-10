from itertools import product

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscribers, CartItem, Cart
from .models import Product
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, Wishlist, ProductImages, ProductReview


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
    #product = Product.objects.get(pid=pid)
    product = get_object_or_404(Product, pid=pid)

#    p_image = product.p_images.all()

#    context = {
#        "p": product,
 #       "p_image":p_image,
 #   }

    return render(request, "core/product-detail.html", {'product': product})


#########################cart###################################

def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    context  = {
        'cart': cart,
        'cart_items': cart.items.all(),
        'total_price': cart.get_total_price(),
    }

    return render(request, "core/cart.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect("cart")


def update_cart_item(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        action = request.POST.get("action")
        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
        return JsonResponse({"success": True, "new_quantity": cart_item.quantity})
    return JsonResponse({"success": False})


def product_page(request):
    products = Product.objects.all()
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, "core/index.html", {"products": products, "cart": cart})