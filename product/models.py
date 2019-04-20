from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category-detail', kwargs={'slug':self.slug})

def category_slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    return instance.slug

pre_save.connect(category_slug_pre_save, sender=Category)


class LocalCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'local category'
        verbose_name_plural = 'local categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:local-category-detail', kwargs={'local_slug':self.slug})


def local_category_slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    return instance.slug

pre_save.connect(local_category_slug_pre_save, sender=LocalCategory)


class Types(models.Model):
    category = models.ForeignKey(LocalCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=300, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:local-types-detail', kwargs={'local_type':self.slug})

def type_slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    return instance.slug

pre_save.connect(type_slug_pre_save, sender=Types)


class Product(models.Model):
    category = models.ForeignKey(Types, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=550, db_index=True, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='product/%Y/%m%d', default='no_image.jpg', )
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} in category {self.category}'

    def get_absolute_url(self):
        pass

def product_slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = f'{slugify(instance.name)}-{instance.pk}'
        return instance.slug

pre_save.connect(product_slug_pre_save, sender=Product)
