from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('signup/', views.signup, name='signup'),  # Added comma and trailing slash for consistency
    path('signin/', views.signin, name='signin'),  # Added comma and trailing slash for consistency
    path('signout/', views.signout, name='signout')  # Added trailing slash for consistency
]
