from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('cancel/', CanceledTemplateView.as_view(), name='order_canceled'),
    path('success/', SuccessTemplateView.as_view(), name='order_success'),
]
