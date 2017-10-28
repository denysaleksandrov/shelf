import os
import operator
import json
import uuid

from django.shortcuts import get_object_or_404, redirect, render
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.core import serializers
from django.views import generic
from django.forms.models import inlineformset_factory
from django.db.models import Q, Count
from django.http import JsonResponse
from django.core.management.base import CommandError
from django.utils.six import StringIO
from bookshelf.models import Book

class BookIndexView(generic.ListView):
    model = Book 
    context_object_name = 'books'
    header_text = 'Books'
    paginate_by = 20
    raise_exception = True
    object_count = None
    template_name = 'book_list.html'

    def get_queryset(self):
        qs = Book.objects.all()
        self.object_count = qs.count()
        return qs

    def get_context_data(self, **kwargs):
        data = super(BookIndexView, self).get_context_data(**kwargs)
        data['header_text'] = self.header_text
        data['object_count'] = self.object_count
        return data
