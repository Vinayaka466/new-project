from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Watches,WatchesUploads,Wishlist,Cart
from.forms import UploadForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def Home(request):
    Watches=WatchesUploads.objects.all()
    context = {'watches_t': Watches}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def Upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()



    return render(request,'upload.html', {'form': form} )

#LOGIN

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user=authenticate(username = user_name , password = password )

            if user is not  None:
                login(request,user)
                return redirect('home')
            else:
                return redirect(request,'login.html',{'form':form})
            
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

#LOGOUT

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

from django.shortcuts import get_object_or_404

def show_product(request,id):
    product = get_object_or_404(WatchesUploads,id=id)
    return render(request,'product.html',{'product':product})

def addtowish(request, id):
    user = request.user
    product = WatchesUploads.objects.get(id=id)
    obj1, created = Wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def show_list(request):
    user = request.user
    wish_object = Wishlist.objects.get(user=user)
    return render(request, "wishlist.html", {"user_products": wish_object.products.all()})

def removewish(request, id):
    product_rm = WatchesUploads.objects.get(id=id)
    wish_obj = Wishlist.objects.get(user = request.user)
    wish_obj.products.remove(product_rm)
    return render(request, 'wishlist.html',{"user_product":wish_obj.products.all()})

def addtocart(request, id):
    user = request.user
    product = WatchesUploads.objects.get(id=id)
    obj1, created = Cart.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def show_cart(request):
    user = request.user
    cart_object = Cart.objects.get(user=user)
    return render(request, "cart.html",{"user_products": cart_object.products.all()})

def removecart(request,id):
    product_rm = WatchesUploads.objects.get(id=id)
    cart_obj = Cart.objects.get(user=request.user)
    cart_obj.products.remove(product_rm)
    return render(request,"cart.html",{"user_products": cart_obj.products.all()})















  
            




