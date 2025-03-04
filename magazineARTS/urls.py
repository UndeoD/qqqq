
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from magazineARTS import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
]

if settings.DEBUG:
    urlpatterns += [
        path('debug/', include('debug_toolbar.urls'))
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

