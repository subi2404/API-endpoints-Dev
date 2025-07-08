from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe
from .serializers import RecipeSerializer

# 1. All recipes (paginated and sorted only)
class RecipeListAllView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'title', 'prep_time', 'total_time']

# 2. Search with filters
class RecipeSearchView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = {
        'rating': ['gte', 'lte'],
        'prep_time': ['gte', 'lte'],
        'cook_time': ['gte', 'lte'],
        'total_time': ['gte', 'lte'],
        'cuisine': ['exact'],
        'serves': ['exact']
    }
    search_fields = ['title', 'description']
    ordering_fields = ['rating', 'title', 'prep_time', 'total_time']
