from django.urls import path, include
from core import views



urlpatterns = [
    # Store Pages
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('blog/', views.blog, name="blog"),
    path('cart/', views.cart, name="cart"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('product/', views.product, name="product"),
    path('product/<slug:slug>', views.product_details, name="product_detail"),
    path('account/my-account/logout/', include('django.contrib.auth.urls')),


    # Account
    path('account/my-account/', views.my_account, name="myaccount"),
    path('account/my-account/', views.register, name="register"),
    path('account/my-account/', views.user_login, name="login"),

    

    # Error page 
    path('404/', views.errors, name="404"),
]