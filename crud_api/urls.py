from django.contrib import admin
from django.urls import include, path
from .views import book, book_detail, ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'review', ReviewViewSet, basename='review')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('book/', book),
    path('book/<int:id>', book_detail),
]