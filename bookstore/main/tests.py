from django.test import TestCase
from .models import Book, Customer, Transaction

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='Test Book', author='Test Author', price=50)

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEqual(expected_object_name, 'Test Book')
