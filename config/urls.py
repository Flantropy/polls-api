from django.contrib import admin
from django.urls import path, include, re_path
from polls.views import home_page
urlpatterns = [
    path('', home_page, name='home-page'),
    path('admin/', admin.site.urls, name='admin-panel'),
    re_path(r'^api/', include('polls.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
