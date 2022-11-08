from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from core.models import *


class ProductAdminForm(forms.ModelForm):
    information = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(widget=CKEditorUploadingWidget())    
    class Meta:
        model = Product 
        fields = '__all__'


class Product_Images(admin.TabularInline):
    model = Product_Image


class Additional_Informations(admin.TabularInline):
    model = Additional_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Informations)
    form = ProductAdminForm
    list_display = ('product_name','price','Categories','section')
    #list_editable = ('Categories', 'section')



admin.site.register(Slider)
admin.site.register(Baner)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Color)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
admin.site.register(Popular_Section)
admin.site.register(Blog_Category)
admin.site.register(Recommended)

