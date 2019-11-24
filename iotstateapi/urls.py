from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .views import StateViewSet

router = routers.DefaultRouter()
router.register(r'state', StateViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
