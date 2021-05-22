from django.test import TestCase

from supersub.models.category import Category


class CategoryTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_category()
    
    @classmethod
    def emulate_category(cls):
        Category.objects.create(
            id=1,
            name="CategorieOne",
            url="www.categorie_test.com")
    
    def test_category_with_category(self):
        category = Category.objects.get(pk=1)
        self.assertIsInstance(category, Category)
    
    def test_category_with_attr_id_is_unique(self):
        category = Category.objects.get(pk=1)
        unique_field = category._meta.get_field('name').unique
        self.assertEquals(unique_field, True)
    
    def test_category_with_attr_name_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
    
    def test_category_with_attr_url_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)
    
    def test_category_with_attr_id(self):
        category = Category.objects.get(pk=1)
        self.assertEquals(category.id, 1)
    
    def test_category_with_attr_name(self):
        category = Category.objects.get(pk=1)
        self.assertEquals(category.name, "CategorieOne")
    
    def test_category_with_attr_url(self):
        category = Category.objects.get(pk=1)
        self.assertEquals(category.url, "www.categorie_test.com")
    
