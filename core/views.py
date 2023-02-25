from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from . models import Product, Customer, PostMessageContact, Cart
from . forms import CustomerRegistrationForm, CustomerProfileForm, PostMessageContactForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
import json
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import get_user_model

# Create your views here.


def home(request):
    return render(request,'home.html' , locals())

def aboutUs(request):
    return render(request,'about.html')

class ContactUsView(View):
    def get(self, request):
        form = PostMessageContactForm()
        return render(request, 'contact.html', locals())
    def post(self, request):
        form =  PostMessageContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            post = PostMessageContact(name = name, email = email, content = content)
            post.save()
            messages.success(request, 'Congratulations! Email Sent Successfully')
        else:
            messages.warning(request, 'Invalid Input Data!')
        return redirect('contact')

def shop(request):
    return render(request,'shop.html')

class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category = val)
        paginator = Paginator(products, 12) # 10 records per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        title = Product.objects.filter(category = val).values('title')
        return render(request, 'category.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product-detail.html', locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customer-registration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! User Register Successfully')
        else:
            messages.warning(request, 'Invalid Input Data!')
        return render(request, 'customer-registration.html', locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile/address/add-address.html', locals())
    def post(self, request):
        form =  CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = user,name = name, locality = locality, city = city, mobile = mobile, state = state, zipcode = zipcode)
            reg.save()
            messages.success(request, 'Congratulations! Profile save Successfully')
        else:
            messages.warning(request, 'Invalid Input Data!')
        return render(request, 'profile/address/add-address.html', locals())

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'profile/address/addresses.html', locals())

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'profile/address/update-address.html', locals())
    def post(self, request, pk):
        form =  CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Congratulations! Profile save Successfully')
        else:
            messages.warning(request, 'Invalid Input Data!')
        return redirect('addresses')


def add_to_cart(request):
    # Retrieve the product from the database
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    # Check if the cart is associated with an authenticated user
    if user.is_authenticated:
        # Retrieve the cart associated with the current user
        # Save the cart
        Cart(user=user, product=product).save()
    else:
        # Retrieve the cart associated with the anonymous user's session
        session_key = request.session.session_key
        if not session_key:
            # Create a new session if one does not exist
            request.session.create()
            session_key = request.session.session_key
        session = SessionStore(session_key=session_key)
        cart_items = session.get('cart', [])
        cart_items.append(product_id)
        session['cart'] = cart_items
        session.save()
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return redirect('show-cart')


def show_cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart = request.session.get('cart', {})
        cart_items = []

        for product_id, item_data in cart.items():
            cart_items.append({
                'product': {
                    'title': item_data['title'],
                    'discounted_price': item_data['discounted_price'],
                },
                'quantity': item_data['quantity'],
                'amount': item_data['discounted_price'] * item_data['quantity'],
            })
    amount = 0
    for p in cart_items:
        value = p.quantity * p.product.discounted_price
        amount += value
    if amount == 0 :
        total_amount = 0
        shipping = 0
    elif amount >= 500 :
        total_amount = amount
        shipping = 0
    else:
        shipping = 50.00
        total_amount = amount + shipping

    return render(request, 'add-to-cart.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        if amount == 0 :
            total_amount = 0
            shipping = 0
        elif amount >= 500 :
            total_amount = amount
            shipping = 0
        else:
            shipping = 50.00
            total_amount = amount + shipping
        data = {
            'quantity': c.quantity,
            'shipping': shipping,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        if amount == 0 :
            total_amount = 0
            shipping = 0
        elif amount >= 500 :
            total_amount = amount
            shipping = 0
        else:
            shipping = 50.00
            total_amount = amount + shipping
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
            'shipping': shipping,
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        if amount == 0 :
            total_amount = 0
            shipping = 0
        elif amount >= 500 :
            total_amount = amount
            shipping = 0
        else:
            shipping = 50.00
            total_amount = amount + shipping
        data = {
            'amount': amount,
            'total_amount': total_amount,
            'shipping': shipping,
        }
        return JsonResponse(data)

class CheckoutView(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        shipping_price = 50.00
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount += value
        if famount >= 500 :
            total_amount = famount
            shipping_price = 0
        else:
            total_amount = famount + shipping_price
        return render(request, 'checkout.html', locals())



