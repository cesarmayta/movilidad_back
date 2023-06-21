from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()

router.register(r'parentesco',
                views.ParentescoViewSet,
                basename='parentesco')

urlpatterns = router.urls