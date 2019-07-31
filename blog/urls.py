from django.contrib import admin
from django.urls import path, include
import blogapp.views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

