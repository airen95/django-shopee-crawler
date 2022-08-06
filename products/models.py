from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    no = models.IntegerField('No', primary_key=True, help_text='product id')
    des = models.TextField('Description')
    cate = models.CharField('Category', max_length=100, help_text='category')
    # info['title'], info['des'], info['cate'], info['price'], info['price_before_discount'], info['variations'], info['images']
    # title = models.CharField('TITLE', max_length=300, )
    # writer = models.CharField('WRITER', max_length=100, help_text='publisher')
    # preview = models.TextField('PREVIEW', unique=True)
    # published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'products'
