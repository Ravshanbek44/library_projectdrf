from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book, Category
from .serializers import BookSerializer, BookCategorySerializer

from rest_framework import generics


# class BookListApiView(generics.ListAPIView):
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         queryset = Book.objects.all()
#         search = self.request.GET.get('search')
#         search1 = self.request.GET.get('id')
#         if search:
#             queryset = queryset.filter(title__icontains=search)
#         if search1:
#             queryset = queryset.filter(id__icontains=search1)
#         return queryset

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        search = self.request.GET.get('search')
        if search:
            books = books.filter(title__icontains=search)
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"return {len(books)} books",
            'books': serializer_data
        }
        return Response(data)

class BookDetailApiView(APIView):

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer_data = BookSerializer(book).data
        context = {
            'status': 'sucessfully',
            "book": serializer_data
        }
        return Response(context)

class BookDeleteApiView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return Response('book is deleted')


class BookCreateApiView(APIView):

    def post(self, request):
        text = request.data
        serializer = BookSerializer(data=text)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            context = {
                'status': "book is saved to database",
                'books': serializer.data
            }
            return Response(context)
        return Response("validatsiyadan o'tmadi")


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        text = request.data
        serializer = BookSerializer(instance=book, data=text, partial=True)
        if serializer.is_valid():
            book_saved = serializer.save()
        return Response(book_saved)

class BookViewSet(ModelViewSet):  # CRUD operations /////////////////////////////////////////////////////////////////////////
    queryset = Book.objects.all()
    serializer_class = BookSerializer

