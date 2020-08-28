from django.urls import path
from .views import HomeView, ProductList, About, CategoryList, customer_detail_form

from blog.views import ArticleList, ArticleDetail

urlpatterns = [
    path('category/<int:id>', CategoryList.as_view(), name='filter'),
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductList.as_view(), name='productlist'),
    path('detail', customer_detail_form, name='detail'),
    path('blog/', ArticleList.as_view(), name='list'),
    path('blog/<int:id>',ArticleDetail.as_view(), name='detail'),
    path('about/', About.as_view(), name='about'),
]