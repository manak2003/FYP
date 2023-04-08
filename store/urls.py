from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('store/', views.StorePage, name='store'),
    path('product/', views.add_product, name='product'),
    path('order/', views.add_order, name='order'),
    path('orderitem/', views.OrderItemPage, name='orderitem'),
    path('orderitem/<int:id>', views.OrderItemPage, name='orderitem'),
    path('orderitem/<int:id>/delete', views.OrderItemPage, name='orderitem'),
    path('delivery/', views.DeliveryPage, name='delivery'),
    path('settings/', views.SettingsPage, name='settings'),  
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

