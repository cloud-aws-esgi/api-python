from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .views import NotificationViewSet

router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
