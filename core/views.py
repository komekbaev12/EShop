from django.shortcuts import render, redirect
from core.models import Slider, Baner, Main_Category, Product,Category,Color, Popular_Section, Recommended,Blog_Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def errors(request):
    return render(request, '404.html')


def home(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]

    # Baner
    baners = Baner.objects.all().order_by('-id')[0:3]
    main_baners = Baner.objects.all().order_by('-id')[0:2]

    # Category
    main_category = Main_Category.objects.all()
    popular = Popular_Section.objects.all()[0:6]

    # Products Section
    products = Product.objects.filter(section__name = "Top Deals Of The Day").order_by('-id')[0:4]
    fproduct = Product.objects.all()[0:4]
    recommended = Recommended.objects.all()


    context ={
        'sliders':sliders,
        'baners':baners,
        'main_category':main_category,
        'products':products,
        'popular':popular,
        'fproduct':fproduct,
        'main_baners':main_baners,
        'recommended':recommended,

    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def blog(request):
    recommended = Recommended.objects.all()
    categories = Blog_Category.objects.all()

    context = {
        'recommended':recommended,
        'categories':categories,
    }

    return render(request, 'blog.html', context)

def blog_details(request, pk):

    blog = Recommended.objects.filter(pk = pk)

    context = {
        'blog':blog
    }

    return render(request, 'blog_details.html',context)


def product(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    colors = Color.objects.all()

    color_id = request.GET.get('colorID')

    if color_id :
        product = Product.objects.filter(color = color_id)
    
    else:
        product = Product.objects.all()

    context = {
        'categories':categories,
        'product':product,
        'colors':colors
    }
    return render(request, 'product/product.html',context)

def contact(request):
    return render(request, 'contact.html')

def product_details(request,slug):
    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'product':product
    }
    return render(request,'product/product-details.html',context)


def my_account(request):
    return render(request, 'registrations/my-account.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'username is ready exists!!!')

            return redirect('myaccount')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email id allready exists!!!')

            return redirect('myaccount')

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        return redirect('myaccount')

        print(email,password)
    return render(request, 'registrations/my-account.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password Are Invalid')
            return redirect('myaccount')
    
    return render(request, 'registrations/my-account.html')



# Differt Pages

def cart(request):
    return render(request,'cart.html')

def wishlist(request):
    return render(request,'wishlist.html')

def faqs(request):
    return render(request, 'faqs.html')


def blog_details(request):
    return render(request, 'blog_details.html')

def checkout(request):
    return render(request, 'checkout.html')

