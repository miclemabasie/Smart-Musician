from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    name = models.CharField(_("Cateogry Name"), max_length=50)
    slug = models.SlugField(verbose_name=_("Slug"), unique=True, help_text="unique value for product page url, created from name")
    description = models.TextField(verbose_name=_("Description"))
    is_active = models.BooleanField(default=True)
    meta_keyword = models.CharField(verbose_name=_("Meta Keyword"), max_length=255)
    meta_description = models.CharField(verbose_name=_("Meta description"), max_length=255, help_text="Comma-delimited set of SEO keywords for meta tag")
    created = models.DateTimeField(verbose_name=_("Date Created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Date Updated"), auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_category", kwargs={"category_slug": self.slug})
    


class Product(models.Model):
    name = models.CharField(verbose_name=_("Product Name"), max_length=200)
    slug = models.SlugField(verbose_name=_("Slug"), unique=True, help_text="unique value for product page url, created from name")
    brand = models.CharField(verbose_name=("Brand Name"), max_length=200)
    sku = models.CharField(verbose_name=_("Sku"), max_length=50)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=9, decimal_places=2)
    old_price = models.DecimalField(verbose_name=_("Old Price"), max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)
    sale_price = models.DecimalField(verbose_name=_("Sale Price"))
    image = models.ImageField(verbose_name=_("Product Image"))
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    description = models.TextField(verbose_name=_("Description"))
    meta_description = models.CharField(verbose_name=_("Meta Description"), max_length=250)
    meta_keywords = models.CharField(verbose_name=("Meta Keywords"), max_length=200)
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    created = models.DateTimeField(verbose_name=_("Date Created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Date Updated"), auto_now=True)

    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"
        ordering = ['-created']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_product", kwargs={"product_slug": self.slug})
    
    def sale_price(self):
        if self.orl_price > self.price:
            return self.price
        else:
            return None


