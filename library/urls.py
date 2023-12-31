from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApiView, BookCreateApiView, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, \
    BookViewSet

# router = SimpleRouter()
# router.register('books', BookViewSet, basename="books")


urlpatterns = [
    path('', BookListApiView.as_view(), ),
    path('create/', BookCreateApiView.as_view(), ),
    path('<int:pk>/', BookDetailApiView.as_view(), ),
    path('delete/<int:pk>/', BookDeleteApiView.as_view(), ),
    path('update/<int:pk>/', BookUpdateApiView.as_view(), ),

]

# urlpatterns = urlpatterns + router.urls
