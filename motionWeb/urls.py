from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from .yasg import urlpatterns as doc_urls


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('motionApp.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
] 

urlpatterns += doc_urls