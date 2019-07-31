from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as accounts_views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logout/', auth_views.auth_logout, {'next_page':'/'}),
    path('signup/', accounts_views.signup, name='signup'),
]

