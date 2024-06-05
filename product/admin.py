from django.contrib import admin
from product.models import Category, ProductColor, ProductSize, Product, ProductFile

admin.site.register(Category)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(ProductFile)
admin.site.register(Product)
