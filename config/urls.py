from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'docs/', include_docs_urls(title='Polls API'), name='docs'),
    re_path(r'^', include('polls.urls')),
]
