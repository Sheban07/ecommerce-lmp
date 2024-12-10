from django.urls import path
from core.views import index, category_list_view, product_list_view, product_detail_view
from . import views
from core import views
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),
    path("category/", category_list_view, name="category-list"),
    path('product/<int:pid>', views.product_detail_view, name="product-detail"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path("cart/", views.cart_view, name="cart"),  # Cart page
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),  # Add to cart
]