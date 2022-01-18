from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginto, name="login"),
    path('post/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.userlogout, name="logout"),
    path('forgot/', views.forgot, name="forgot"),
]
