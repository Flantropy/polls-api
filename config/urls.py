from django.contrib import admin
from django.urls import path, include, re_path
urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    re_path(r'^', include('polls.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
