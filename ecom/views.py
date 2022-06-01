from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout,login
from django.views.generic import CreateView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    cat=Category.objects.all() 
    return render(request,'ecom/home.html',{'category':cat})

def product(request,pk):
    prod=Product.objects.filter(catid=pk)

    if request.user.is_authenticated:
        item_already= []
        for i in prod:
            if Cart.objects.filter(Q(product=i.id) & Q(user=request.user)):
                item_already.append(i.name)
        
        return render(request,'ecom/product.html',{'product':prod,"item_already":item_already})
    return render(request,'ecom/product.html',{'product':prod})

@login_required
def add_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')

    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
    if cart:
        cart_prod_total=[]
        for i in Cart.objects.all():
            if i.user==user:
                cart_prod_total.append(i.quantity * i.product.price)
        if sum(cart_prod_total)>10000:
            total_price=sum(cart_prod_total)-500
        else:
            total_price=sum(cart_prod_total)
        return render(request,'ecom/addcart.html',{'carts':cart,'total':sum(cart_prod_total),'totalp':total_price})    

    else:
        return render(request,'ecom/emptycart.html')

@login_required
def plus_cart(request):
    if request.method =='GET':
        pid=request.GET['prod_id']
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.quantity+=1
        c.save()

        cart_prod_total=[]
        for i in Cart.objects.all():
            if i.user==request.user:
                cart_prod_total.append(i.quantity * i.product.price)
        total_price=sum(cart_prod_total)
        if sum(cart_prod_total)>10000:
            total_price=sum(cart_prod_total)-500
        else:
            total_price=sum(cart_prod_total)
        data={'quantity':c.quantity,'total':sum(cart_prod_total),'totalp':total_price}
        
        return JsonResponse(data)


@login_required
def minus_cart(request):
    if request.method =='GET':
        pid=request.GET['prod_id']
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.quantity-=1
        c.save()

        cart_prod_total=[]
        for i in Cart.objects.all():
            if i.user==request.user:
                cart_prod_total.append(i.quantity * i.product.price)
        
        if sum(cart_prod_total)>10000:
            total_price=sum(cart_prod_total)-500
        else:
            total_price=sum(cart_prod_total)
        data={'quantity':c.quantity,'total':sum(cart_prod_total),'totalp':total_price}
        return JsonResponse(data)

@login_required       
def remove_cart(request):
    if request.method =='GET':
        pid=request.GET['prod_id']
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.delete()

        cart_prod_total=[]
        for i in Cart.objects.all():
            if i.user==request.user:
                cart_prod_total.append(i.quantity * i.product.price)
        
        if sum(cart_prod_total)>10000:
            total_price=sum(cart_prod_total)-500
        else:
            total_price=sum(cart_prod_total)
        data={'total':sum(cart_prod_total),'totalp':total_price}
        return JsonResponse(data)

def logouts(request):
    logout(request) 
    return redirect('categorypage')



@login_required
def generate_bill(request):
    cart=Cart.objects.filter(user=request.user)
    total_anount=[]
    quantity=len(cart)
    products=""
    for i in cart:
        a=i.product.price * i.quantity
        total_anount.append(a)
        products=products+str(i.product.name)+" "

    if sum(total_anount)>1000:
        discounted_amount=sum(total_anount)-500
        discount=500
    else:
        discounted_amount=sum(total_anount)
        discount=0

    
    UserBill(user=request.user,products=products,quantity=quantity,total_anount=sum(total_anount),discounted_amount=discounted_amount,discout=discount).save()
    for i in cart:
        Bill(user=i.user,product=i.product,quantity=i.quantity).save()
        i.delete()

    return redirect('/my_bill')

def my_bill(request):
    bill=UserBill.objects.filter(user=request.user)
    

    return render(request,"ecom/bill.html",{'bill':bill})


@login_required
def all_bill(request):
    bill=UserBill.objects.all()
    return render(request,'ecom/allbill.html',{'bills':bill})

@login_required
def all_cart(request):
    carts=Cart.objects.all()
    return render(request,'ecom/allcart.html',{'carts':carts})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('categorypage')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="ecom/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('categorypage')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="ecom/login.html", context={"login_form":form})


class Addproduct(CreateView):
    template_name='ecom/addproduct.html'
    model=Product
    fields=['name','desc','price','image','catid']
    context_object_name='form'

class Addcategory(CreateView):
    template_name='ecom/addcategory.html'
    model=Category
    fields=['name','image']
    context_object_name='form'