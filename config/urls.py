from django.contrib import admin
from django.urls import path, include
from polls.views import home_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('admin/', admin.site.urls, name='admin-panel'),
    path('api/', include('polls.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
