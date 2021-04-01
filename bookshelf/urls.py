from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from bookshelf import views

app_name = 'bookshelf'
schema_view = get_swagger_view(title='Shelf API')

urlpatterns = [url(r'^$',
                   views.BookIndexView.as_view(),
                   name='Book_index'),
               url(r'^api-view/$', schema_view),
              ]
