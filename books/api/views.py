from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    get_object_or_404)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    BookSerializer,
    BookCreateUpdateSerializer,
)

from books.models import Book
from django.contrib.auth.models import User


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class BookUpdateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer


#List all the books in the data base
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Book.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(Title__icontains=query)|
                Q(Author_Name__icontains=query)
            )
        return queryset_list



#list book's details
class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FavouriteBookView(APIView):

    serializer_class = BookSerializer

    def get(self, request, pk = None, format=None):
        selected_book = get_object_or_404(Book, id=pk)
        current_user = User.objects.get(id=request.user.id)

        if current_user in selected_book.Users.all():
            selected_book.Users.remove(request.user)
        else:
            selected_book.Users.add(request.user)
        selected_book.save()
        return Response("Book added to the favourites")



    # def get(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    #     obj = get_object_or_404(queryset, **filter_kwargs)
    #
    #     obj.Users.add(self.user)
    #     obj.save()
    #     return obj




