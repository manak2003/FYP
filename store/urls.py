from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.StorePage, name='store'),
    path('product/', views.ProductPage, name='product'),
    path('order/', views.OrderPage, name='order'),
    path('orderitem/', views.OrderItemPage, name='orderitem'),
    path('orderitem/<int:id>', views.OrderItemPage, name='orderitem'),
    path('orderitem/<int:id>/delete', views.OrderItemPage, name='orderitem'),
    path('delivery/', views.DeliveryPage, name='delivery'),
    path('settings/', views.SettingsPage, name='settings'),  
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]