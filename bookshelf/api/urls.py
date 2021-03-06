from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from bookshelf.api.views import BookViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'bookshelf', BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
