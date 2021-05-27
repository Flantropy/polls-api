from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    path('api/', include('polls.urls'), name='api-root')
]
