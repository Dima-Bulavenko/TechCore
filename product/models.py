from django.db import models
from django.urls import reverse

from product import CategoryChoices, CPUAttributeChoices, GPUAttributeChoices, ManufacturerChoices
from product.managers import ProxyProductManager
from product.utils import ProductCategoryMapper
from users.models import User

product_category_mapper = ProductCategoryMapper()


class Category(models.Model):
    name = models.CharField(max_length=100, choices=CategoryChoices, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_list", kwargs={"category": self.name})


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
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    @property
    def rating(self):
        if reviews := self.reviews.all():
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0

    @property
    def review_count(self):
        return self.reviews.count()
    
    @property
    def review_data(self) -> dict:
        review_data = {}
        reviews = self.reviews.all()
        review_data['reviews'] = reviews.order_by('-created_at')
        review_data['reviews_count'] = self.review_count
        review_data['rating'] = self.rating
        review_data['rating_summary'] = self.rating_summary
        return review_data
    
    @property
    def rating_summary(self) -> dict:
        reviews = self.reviews.all()
        total_reviews = reviews.count()
        rating_summary = {}

        for rating in range(1, 6):
            rating_count = reviews.filter(rating=rating).count()
            rating_percentage = round((rating_count / total_reviews) * 100 if total_reviews else 0)
            rating_summary[rating] = {
                'count': rating_count,
                'percentage': rating_percentage if rating_percentage else 0
            }
        return dict(sorted(rating_summary.items(), reverse=True))
    
    @property
    def product_title(self) -> str:
        messages_placeholders = []
        title_names = [n.value for n in self.title_attributes()]
        for pr_ar in self.productattributevalue_set.all():
            if pr_ar.attribute.name in title_names:
                messages_placeholders.append(pr_ar.value)  # noqa: PERF401
        return self.title_format.format(self.name, *messages_placeholders)


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
    attrs = CPUAttributeChoices
    objects = ProxyProductManager()

    class Meta:
        proxy = True
        verbose_name = 'CPU product'

    @property
    def title_format(self) -> str:
        return "{0}, {1} Core, {2} Thread, {3}, {4}"
    
    @classmethod
    def title_attributes(cls) -> list:
        attrs = cls.attrs
        return [
            attrs.CORE_COUNT,
            attrs.THREAD_COUNT,
            attrs.BASE_CLOCK_SPEED,
            attrs.TDP,
        ]
    
    @classmethod
    def get_filter_attributes(cls):
        attrs = cls.attrs
        return [
            attrs.CORE_COUNT,
            attrs.THREAD_COUNT,
            attrs.BASE_CLOCK_SPEED,
            attrs.BOOST_CLOCK_SPEED,
            attrs.TDP,
            attrs.INTEGRATED_GRAPHICS
        ]


@product_category_mapper(category=CategoryChoices.GPU)
class GPUProduct(ProductMixin, Product):
    _category = CategoryChoices.GPU
    attrs = GPUAttributeChoices

    objects = ProxyProductManager()

    class Meta:
        proxy = True
        verbose_name = 'GPU product'
    
    @property
    def title_format(self) -> str:
        return "{0}, {1} Memory, {2}, {3}"
    
    @classmethod
    def title_attributes(cls) -> list:
        attrs = cls.attrs
        return [
            attrs.MEMORY_SIZE,
            attrs.MEMORY_TYPE,
            attrs.OUTPUTS,
        ]
    
    @classmethod
    def get_filter_attributes(cls):
        attrs = cls.attrs
        return [
            attrs.MEMORY_SIZE,
            attrs.MEMORY_TYPE,
            attrs.BASE_CLOCK_SPEED,
            attrs.BOOST_CLOCK_SPEED,
            attrs.GPU_ARCHITECTURE,
        ]


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.author}"
