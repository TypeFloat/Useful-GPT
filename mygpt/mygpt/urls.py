from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('member/', include('member.urls')),
    path('papers/', include('papers.urls')),
    path('admin/', admin.site.urls),
]
