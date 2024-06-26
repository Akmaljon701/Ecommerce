from django.db import models

from user.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='product_sizes', on_delete=models.PROTECT)

    def __str__(self):
        return self.size


class Product(models.Model):
    SEASON_CHOICES = [
        ('Spring', 'Bahor'),
        ('Summer', 'Yoz'),
        ('Fall', 'Kuz'),
        ('Winter', 'Qish'),
    ]
    SEX_CHOICES = [
        ('Male', 'Erkak'),
        ('Female', 'Ayol'),
    ]
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    colors = models.ManyToManyField(ProductColor, related_name='product_colors')
    sizes = models.ManyToManyField(ProductSize, related_name='product_sizes')
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.PROTECT)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    info = models.TextField()

    liked_by = models.ManyToManyField(CustomUser, related_name='liked_products', blank=True)
    favorited_by = models.ManyToManyField(CustomUser, related_name='favorite_products', blank=True)

    def __str__(self):
        return self.name


class ProductFile(models.Model):
    file = models.FileField(upload_to='product/')
    product = models.ForeignKey(Product, related_name='product_files', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} - {self.file.url}'




