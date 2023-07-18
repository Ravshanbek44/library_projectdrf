from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book, Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'author', 'isbn', 'price', 'category']

    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)
        prise = data.get('price', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Book's title contains only chars"
                }
            )
        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    "status": False,
                    "message": "Book's title and auth mus not be the same!"
                }
            )

        return data


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

    def validate(self, data):
        name = data.get("name", None)
        if not name.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Book's category contains only chars"
                }
            )

        return data
