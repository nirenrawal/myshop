from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #FOR IMAGES
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #FOR IMAGES
