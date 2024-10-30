from datetime import date
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from product.models import (
    Attribute,
    Category,
    Manufacturer,
    Product,
    ProductAttributeValue,
)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Electronics")
        cls.manufacturer = Manufacturer.objects.create(name="TechCo")
        cls.attribute = Attribute.objects.create(name="Color")

    def test_create_product(self):
        product = Product.objects.create(
            name="Test Product",
            price=Decimal("99.99"),
            description="A test product",
            category=self.category,
            manufacturer=self.manufacturer,
            weight=Decimal("1.234"),
            dimensions="10x20x30",
            release_date=date(2023, 1, 1),
        )
        product.attributes.add(self.attribute)

        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, Decimal("99.99"))
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.manufacturer, self.manufacturer)
        self.assertIn(self.attribute, product.attributes.all())
        self.assertEqual(product.weight, Decimal("1.234"))
        self.assertEqual(product.dimensions, "10x20x30")
        self.assertEqual(product.release_date, date(2023, 1, 1))
        self.assertIsNotNone(product.created_at)
        self.assertIsNotNone(product.updated_at)

    def test_unique_together_constraint(self):
        Product.objects.create(
            name="Unique Product",
            price=Decimal("59.99"),
            category=self.category,
            manufacturer=self.manufacturer,
        )

        duplicate_product = Product(
            name="Unique Product",
            price=Decimal("79.99"),
            category=self.category,
            manufacturer=self.manufacturer,
        )

        with self.assertRaises(ValidationError):
            duplicate_product.full_clean()  # Checks unique_together validation

    def test_str_method(self):
        product = Product.objects.create(
            name="Sample Product",
            price=Decimal("49.99"),
            category=self.category,
            manufacturer=self.manufacturer,
        )
        self.assertEqual(str(product), "Sample Product")

    def test_get_absolute_url(self):
        product = Product.objects.create(
            name="Product URL Test",
            price=Decimal("29.99"),
            category=self.category,
            manufacturer=self.manufacturer,
        )
        self.assertEqual(
            product.get_absolute_url(),
            reverse("product_detail", kwargs={"pk": product.pk}),
        )

    def test_blank_optional_fields(self):
        product = Product.objects.create(
            name="Blank Fields Product",
            price=Decimal("19.99"),
            category=self.category,
            manufacturer=self.manufacturer,
        )

        self.assertIsNone(product.weight)
        self.assertEqual(product.dimensions, "")
        self.assertIsNone(product.release_date)
