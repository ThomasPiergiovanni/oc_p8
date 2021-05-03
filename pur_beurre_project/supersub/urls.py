from django.urls import path

# from .views import ProductDetailView, FavoritesView, RegisterFavoriteView, LegalMentionsView
from .views.favorites_view import FavoritesView
from .views.index_view import IndexView
from .views.legal_mentions_view import LegalMentionsView
from .views.product_detail_view import ProductDetailView
from .views.register_favorite_view import RegisterFavoriteView
from .views.result_view import ResultView

app_name = 'supersub'

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    path('product_detail/<int:id_product>', ProductDetailView.as_view(), name='product_detail'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('results/', ResultView.as_view(), name='results'),
    path('register_favorite/<int:id_product>', RegisterFavoriteView.as_view(), name='register_favorite' ),
    path('legal_mentions/', LegalMentionsView.as_view(), name='legal_mentions')
]
