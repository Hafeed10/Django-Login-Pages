from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Ensure the trailing slash
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
