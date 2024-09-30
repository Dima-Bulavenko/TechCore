from django.contrib.postgres.search import SearchQuery, SearchVector

from product.models import Product


class ProductSearch:
    def __init__(self, query):
        self.query = query

    def search(self):
        search_vector = SearchVector(
            "manufacturer__name", 
            "name",
            "category__name",
            "description",
        )
        search_query = SearchQuery(self.query)
        return Product.objects.annotate(search=search_vector).filter(search=search_query)
