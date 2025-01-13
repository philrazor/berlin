from django.urls import path
from .views import home, search_results, signup, custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'), 
    path('search_results', search_results, name='search'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
]