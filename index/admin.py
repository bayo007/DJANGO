from django.contrib import admin
from .models import About, Slider, App, Brand, Product
# Register your models here.

admin.site.register(App)
admin.site.register(About)
admin.site.register(Slider)
admin.site.register(Brand)
admin.site.register(Product)