import os
import operator
import contextlib
from functools import reduce

from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer

from bookshelf.models import Book
from bookshelf.api.serializers import BookSerializer
from bookshelf.api.renderers import BookJSONRenderer


class BookViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all() 
    renderer_classes = (BrowsableAPIRenderer, BookJSONRenderer,)

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(
                author__icontains=author
            )

        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(
                title__icontains=title
            )


        return queryset

    def create(self, request):
        #print(request.__dict__)
        #print(request.accepted_renderer.format)
        if request.accepted_renderer.format == 'api':
            fields = [ field.name for field in Book._meta.get_fields() ]
            #print(list(request.data.items()))
            serializer_data = { key:value
                                    for key,value in request.data.items()
                                        if key in fields and value != "" }
        else:
            serializer_data = request.data.get('book', {})
        serializer_context = { 'request': request }
        #print(serializer_data)
        try:
            title = serializer_data['title']
            book = self.queryset.filter(title=title)
            if book:
                raise ValidationError('Book already exist.')
        except KeyError:
            raise ValidationError('Title is not supplied.')

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        serializer_context = {'request': request}
        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound('Book you are seeking for does not exist.')

        serializer_data = request.data.get('book', {})
        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        serializer_context = {'request': request}
        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound('Book you are seeking for does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            book = self.queryset.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound('Book with this ID does not exist.')

        if book.cover:
            image_path = settings.MEDIA_ROOT + "/" + book.cover.name
            with contextlib.suppress(FileNotFoundError):
                os.remove(image_path)
        book.delete()
        

        return Response({}, status=status.HTTP_204_NO_CONTENT)
