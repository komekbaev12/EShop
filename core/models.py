from django.db import models
from django.contrib.auth.models import User





class Slider(models.Model):

    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),
    )


    image = models.ImageField(upload_to='media/slider')
    discount_deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    sale = models.IntegerField()
    brand = models.CharField(max_length=200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.brand


class Baner(models.Model):
    image = models.ImageField(upload_to='media/baner')
    discount_deal = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    discount = models.IntegerField()
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.quote

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " -- " + self.main_category.name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code
    


class Product(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField() 
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    information = models.TextField()
    name = models.CharField(max_length=100)
    Categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE, null=True)
    tags = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug':self.slug})




class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specificational = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)

class Popular_Section(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/cat/',null=True, blank=True)

    
   

class Blog_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recommended(models.Model):

    Categories = models.ForeignKey(Blog_Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='media/blog/',null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
