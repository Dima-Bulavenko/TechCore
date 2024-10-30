from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from product.models import (
    Attribute,
    Category,
    Manufacturer,
    Product,
    ProductAttributeValue,
    Review,
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

        
class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Electronics", description="Electronic items")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic items")

    def test_str_method(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(str(category), "Electronics")

    def test_get_absolute_url(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(
            category.get_absolute_url(),
            reverse("product_list", kwargs={"category": category.name}),
        )

    def test_unique_constraint(self):
        Category.objects.create(name="Electronics")
        with self.assertRaises(ValidationError):
            duplicate_category = Category(name="Electronics")
            duplicate_category.full_clean()  # Checks unique constraint validation


User = get_user_model()


class ReviewModelTest(TestCase):

    def setUp(self):
        # Create necessary related objects
        self.category = Category.objects.create(name="Electronics")
        self.manufacturer = Manufacturer.objects.create(name="Acme Corp")
        self.product = Product.objects.create(
            name="Smartphone",
            price=999.99,
            description="A high-end smartphone",
            category=self.category,
            manufacturer=self.manufacturer,
            weight=0.5,
            dimensions="5x3x0.3 inches",
            release_date="2023-01-01"
        )
        self.user = User.objects.create_user(email='test@gmail.com', password='12345')

    def test_create_review(self):
        review = Review.objects.create(
            product=self.product,
            author=self.user,
            rating=5,
            review="Excellent product!"
        )
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.author, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.review, "Excellent product!")
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_rating_choices(self):
        review = Review.objects.create(
            product=self.product,
            author=self.user,
            rating=3,
            review="Average product"
        )
        self.assertIn(review.rating, [1, 2, 3, 4, 5])

    def test_review_auto_now_add(self):
        review = Review.objects.create(
            product=self.product,
            author=self.user,
            rating=4,
            review="Good product"
        )
        self.assertAlmostEqual(review.created_at, timezone.now(), delta=timezone.timedelta(seconds=1))

    def test_review_auto_now(self):
        review = Review.objects.create(
            product=self.product,
            author=self.user,
            rating=4,
            review="Good product"
        )
        old_updated_at = review.updated_at
        review.review = "Updated review"
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)
