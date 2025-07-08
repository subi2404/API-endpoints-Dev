from django.urls import path
from .views import RecipeListAllView, RecipeSearchView

urlpatterns = [
    path('recipes/', RecipeListAllView.as_view(), name='recipe-list'),
    path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
]
