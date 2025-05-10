from django.shortcuts import render
from .models import About,Slider,Brand,App,Product 

# Create your views here.

def home(request):
    brand = Brand.objects.all()
    app = App.objects.all()
    product = Product.objects.all()
    sliderdata = Slider.objects.all()
    aboutdata = About.objects.all()[0]
    context={
        'about': aboutdata,
        'slider': sliderdata,
        'brand': brand,
        'app': app,
        'product': product
    }
    return render(request, 'index.html',context)
