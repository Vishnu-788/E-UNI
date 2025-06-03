from django.urls import path
from .views import (
    ShopDetailUpdateView,
)

urlpatterns = [
    path('', ShopDetailUpdateView.as_view(), name="shop-detail")
]
