from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import create_discount_code, get_discount_code
from django.urls import path

router = SimpleRouter()

urlpatterns = [
    url('', include(router.urls)),
    url(r'^create', create_discount_code),
    path(r'<id>', get_discount_code),
]
