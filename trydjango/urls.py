
from django.contrib import admin
from django.urls import path
from .views import home_view
from accounts.views import (
    login_view, logout_view, register_view
)
from articles.views import (
    search_view,
    article_view,
    create_view,
)

urlpatterns = [
    path('', home_view, name="home"),
    path('articles/', search_view, name="search-view"),
    path('articles/create/', create_view, name="create-view"),
    path('articles/<int:id>/', article_view, name="article-view"),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    
]
