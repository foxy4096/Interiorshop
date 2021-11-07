from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from apps.vendor.models import Vendor


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return "https://via.placeholder.com/240x180.jpg"
    
    def make_thumbnail(self, image, size=(300, 200)):
        image = Image.open(image)
        image.convert('RGB')
        image.thumbnail(size)

        temp_handle = BytesIO()
        image.save(temp_handle, 'JPEG')
        thumbnail = File(temp_handle, name=f"{self.name}_img_thumb" + '.jpg')
        return thumbnail
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.thumbnail.delete()
        super().delete(*args, **kwargs)
