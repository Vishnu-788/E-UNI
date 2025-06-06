from django.urls import path
from .views import shop_views, customer_views

urlpatterns = [
    path('shop/', shop_views.ShopOrderListView.as_view(), name='order-list-shop'),
    path('shop/<int:pk>/detail/', shop_views.ShopOrderDetailView.as_view(), name='order-detail-shop'),
    path('shop/<int:pk>/update/', shop_views.ShopOrderUpdateView.as_view(), name='order-update-shop'),
    path('shop/<int:pk>/delete/', shop_views.ShopOrderDestroyVIew.as_view(), name='order-destroy-shop'),

    path('customer/', customer_views.CustomerOrderListView.as_view(), name='order-list-customer'),
    path('customer/create/', customer_views.CustomerOrderCreateView.as_view(), name='order-create-customer'),
    path('customer/<int:pk>/detail/', customer_views.CustomerOrderDetailView.as_view(), name='order-detail-customer'),
]
