from django.urls import path
from core.views import index, category_list_view, product_list_view, product_detail_view
from . import views
from core import views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),
    path("category/", category_list_view, name="category-list"),
]