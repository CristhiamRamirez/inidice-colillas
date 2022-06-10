from django.contrib import admin
from django.urls import include,path
from indice import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('indice.urls')),
]
