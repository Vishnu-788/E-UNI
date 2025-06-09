from django.urls import path
from .views import (
    CustomerProfileDetailUpdateView,
    CustomerProductBrowseDetailView,
    CustomerProductBrowseListView
)

urlpatterns = [
    path('profile/', CustomerProfileDetailUpdateView.as_view(), name='customer-profile'),
    path('', CustomerProductBrowseListView.as_view(), name='customer-product-list'),
    path('<int:pk>/', CustomerProductBrowseDetailView.as_view(), name='customer-product-detail'),
]
