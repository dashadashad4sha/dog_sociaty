from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('test/', include('testapp.urls'))
]

if settings.DEBUG:
    from django.urls import include, path

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
