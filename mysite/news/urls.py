from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    #path('test/', test, name='test'),
    path('', HomeNews.as_view(), name='home'),
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('bio/<int:category_id>', ByBio.as_view(), name='doggy'),
    path('news/<int:pk>/', ViewsNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]