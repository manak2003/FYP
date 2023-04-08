from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.conf import settings
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here. 


def StorePage(request):
    data = Product.objects.all()
    return render(request,"store/store.html",{'data': data})

def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        value = form.cleaned_data.get('value')
        discount = form.cleaned_data.get('discount')
        final_value = form.cleaned_data.get('final_value')
        is_paid = form.cleaned_data.get('is_paid')
    
        order = Order(title=title,value=value, discount=discount, final_value=final_value, is_paid=is_paid)
        order.save()
        
    ctx = {
        'title':'OrderPage',
        'form': form
    }
    return render(request,"store/order.html",ctx)

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        image = Image.objects.create(image=request.FILES['image'])
        short_description = form.cleaned_data.get('short_description')
        quantity = form.cleaned_data.get('quantity')
        category = form.cleaned_data.get('category')
        value = form.cleaned_data.get('value')
        discount_value = form.cleaned_data.get('discount_value')
        final_value = form.cleaned_data.get('final_value')
        status = form.cleaned_data.get('status')
        
        product = Product(title=title,image=image,short_description=short_description,quantity=quantity,category=category,value=value,discount_value=discount_value,final_value=final_value, status=status)
        product.save()
        
        messages.success(request, 'Product added successfully')
        return redirect('store')
        
        
        
    ctx = {
        'title':'ProductPage',
        'form': form
    }
    return render(request,"store/product.html",ctx)

def OrderItemPage(request):
    form = OrderItemForm(request.POST or None)
    if form.is_valid():
        product = form.cleaned_data.get('product')
        order = form.cleaned_data.get('order')
        qty = form.cleaned_data.get('qty')
        price = form.cleaned_data.get('price')
        discount_price = form.cleaned_data.get('discount_price')
        final_price = form.cleaned_data.get('final_price')
        total_price = form.cleaned_data.get('total_price')
        
        orderitem = OrderItem(product=product,order=order,qty=qty,price=price,discount_price=discount_price,final_price=final_price,total_price=total_price)
        orderitem.save()
        
    ctx = {
        'title':'OrderPage',
        'form': form
    }
    return render(request,"store/order.html",ctx)

def DeliveryPage(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        value = form.cleaned_data.get('value')
        active = form.cleaned_data.get('active')
        created_at = form.cleaned_data.get('created_at')
        last_modified = form.cleaned_data.get('last_modified')
        
        delivery = Delivery(title=title,value=value,active=active,created_at=created_at,last_modified=last_modified)
        delivery.save()
        
    ctx = {
        'title':'DeliveryPage',
        'form': form
    }
    return render(request,"store/delivery.html",ctx)

def SettingsPage(request):
    return render(request,"store/settings.html")

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=request.session.get('cart_id'), product=product)
    

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    if 'cart_id' not in request.session:
        request.session['cart_id'] = cart.id
        
    cart_count = CartItem.objects.filter(cart=request.session.get('cart_id')).count()
    return JsonResponse({'cart_count': cart_count})



@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart
    product = cart_item.product
    cart_item.delete()
    cart.items.remove(product)
    cart.total -= product.price
    cart.save()

    return redirect('add_to_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {'cart_items': cart_items, 'total': cart.total}
    return render(request, 'store/cart.html', context)
    