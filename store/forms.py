from django import forms
from .models import Product,Category,Image,Order,OrderItem
from tinymce.widgets import TinyMCE

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ('name',)
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')
        
class OrderForm(forms.Form):
    title = forms.CharField(widget=TinyMCE(attrs={'cols':22,'rows':3},),)
    value = forms.DecimalField()
    discount = forms.DecimalField()
    final_value = forms.DecimalField()
    is_paid = forms.BooleanField()
    class Meta:
        model = Order
        fields = ('title','value','discount','final_value','is_paid')
    
class ProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput ,max_length=100)
    short_description = forms.CharField(widget=forms.Textarea,max_length=150, help_text='Describe the product')
    qty = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')
    value = forms.DecimalField()
    discount_value = forms.DecimalField()
    final_value = forms.DecimalField()
    status = forms.ChoiceField(choices=Product.StatusChoice.choices, widget=forms.RadioSelect)
    
    class Meta:
        model = Product
        fields = ('title','short_description','category','qty','value','discount_value','final_value','status')
        
class OrderItemForm(forms.Form):
    product = forms.CharField(widget=forms.TextInput)
    order = forms.CharField(widget=forms.TextInput)
    qty = forms.IntegerField(widget = forms.TextInput)
    price = forms.DecimalField(widget = forms.TextInput)
    discount_price = forms.DecimalField(widget = forms.TextInput)
    final_price = forms.DecimalField(widget = forms.TextInput)
    total_price = forms.DecimalField(widget = forms.TextInput)
    
    class Meta:
        model = OrderItem
        fields = ('product','order','qty','price','discount_price','final_price','total_price')
        
class DeliveryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    value = forms.DecimalField()
    active = forms.BooleanField()
    created_at = forms.DateTimeField()
    last_modified = forms.DateTimeField()
    
    class Meta:
        model = Order
        fields = ('title','value','active','created_at','last_modified')

class SettingsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    logo = forms.ImageField()
    phone = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.TextInput)
    currency = forms.CharField(widget=forms.TextInput)
    created_at = forms.DateTimeField()
    last_modified = forms.DateTimeField()
    
    class Meta:
        model = Order
        fields = ('title','logo','phone','email','address','currency','created_at','last_modified')
        
