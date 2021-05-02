from django.urls import path

from . import views
from .views import IndexView, ProductDetailView, FavoritesView, RegisterFavoriteView, ResutlView, LegalMentionsView

app_name = 'supersub'

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    path('product_detail/<int:id_product>', ProductDetailView.as_view(), name='product_detail'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('results/', ResutlView.as_view(), name='results'),
    path('register_favorite/<int:id_product>', RegisterFavoriteView.as_view(), name='register_favorite' ),
    path('legal_mentions/', LegalMentionsView.as_view(), name='legal_mentions')
]
