class ProductCategoryMapper:
    def __init__(self):
        self.category_class_pair = {}

    def __call__(self, category):
        def decorator(cls):
            # Store the category-class pair in the instance dictionary
            self.category_class_pair[category] = cls
            return cls

        return decorator

    def get_class(self, category):
        return self.category_class_pair.get(category)
