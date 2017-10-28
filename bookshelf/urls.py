from django.conf.urls import url, include
from bookshelf import views

app_name = 'bookshelf'

urlpatterns = [url(r'^$',
                   views.BookIndexView.as_view(),
                   name='Book_index'),
              ]
