from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from userauth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginn),
    path('logout/', views.logoutt),
    path('upload', views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_posts),
    path('profile/<str:id_user>', views.profileView )
]