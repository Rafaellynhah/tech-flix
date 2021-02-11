from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, MovieViewSet, SerieViewSet


router = routers.DefaultRouter()
router.register(r'categories',CategoryViewSet, basename="categories")
router.register(r'movies', MovieViewSet, basename="movies")
router.register(r'series', SerieViewSet, basename="series")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
