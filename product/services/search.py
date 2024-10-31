from django.conf import settings
from django.db.models import Avg, CharField, OuterRef, Q, Subquery, Value
from django.db.models.functions import Concat

from product.models import Image, Product


class ProductSearch:
    def __init__(self, query):
        self.query = query

    def search(self):
        # TODO Refactor, this code was taken from ProductFilter
        queryset = Product.objects.prefetch_related(
            "productattributevalue_set__attribute",
            "reviews",
        ).filter(
            Q(name__icontains=self.query)
            | Q(description__icontains=self.query)
            | Q(manufacturer__name__icontains=self.query)
        )

        images = Image.objects.filter(product=OuterRef("pk"))

        queryset = queryset.annotate(
            image_url=Concat(
                Value(settings.MEDIA_URL),
                Subquery(images.values("image")[:1]),
                output_field=CharField(),
            ),
            rating_avg=Avg("reviews__rating", default=0),
        )
        return queryset
