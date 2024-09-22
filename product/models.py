from django.db import models

from product import CategoryChoices, CPUAttributeChoices, ManufacturerChoices
from product.managers import ProxyProductManager
from product.utils import ProductCategoryMapper
from users.models import User

product_category_mapper = ProductCategoryMapper()


class Category(models.Model):
    name = models.CharField(max_length=100, choices=CategoryChoices, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, choices=ManufacturerChoices, unique=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name='attributes')

    def __str__(self):
        return self.name
    
    def clean(self):
        if hasattr(self, 'name'):
            self.name = self.name.lower()


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images')

    def __str__(self):
        return f"{self.product.name} image"


class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('product', 'attribute')

    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Attribute, through=ProductAttributeValue, related_name='products')
    weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "category")

    def __str__(self):
        return self.name

    @property
    def rating(self):
        if self.reviews.exists():
            return round(self.reviews.aggregate(models.Avg('rating'))['rating__avg'], 1)
        return 0

    @property
    def review_count(self):
        return self.reviews.count()
    
    @property
    def product_title(self):
        concrete_product_class = product_category_mapper.get_class(self.category.name)
        if concrete_product_class:
            concrete_product = concrete_product_class.objects.get(pk=self.pk)
            return concrete_product.__str__()
        return self.__str__()
    
    def get_attribute_value(self, attribute_name: str) -> str:
        try:
            attribute_value = self.productattributevalue_set.get(attribute__name=attribute_name)
            return attribute_value.value
        except ProductAttributeValue.DoesNotExist:
            return None


class ProductMixin:
    @classmethod
    def get_category(cls) -> Category:
        return Category.objects.get(name=cls._category)
    
    @classmethod
    def get_attributes(cls) -> models.QuerySet:
        return cls.get_category().attributes.all()


@product_category_mapper(category=CategoryChoices.CPU)
class CPUProduct(ProductMixin, Product):
    _category = CategoryChoices.CPU

    objects = ProxyProductManager()

    class Meta:
        proxy = True
        verbose_name = 'CPU product'

    def __str__(self):
        core = self.get_attribute_value(CPUAttributeChoices.CORE_COUNT.value)
        thread = self.get_attribute_value(CPUAttributeChoices.THREAD_COUNT.value)
        clock_speed = self.get_attribute_value(CPUAttributeChoices.BASE_CLOCK_SPEED.value)
        tdp = self.get_attribute_value(CPUAttributeChoices.TDP.value)
        return f"{self.manufacturer} {self.name}, {core} Core, {thread} Thread, {clock_speed}, {tdp}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.author}"
