from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Customer, PostMessageContact
from . forms import CustomerRegistrationForm, CustomerProfileForm, PostMessageContactForm
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'home.html')

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
        return render(request, 'profile.html', locals())
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
        return render(request, 'profile.html', locals())

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'address.html', locals())

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'update-address.html', locals())
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
        return redirect('address')
