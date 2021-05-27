from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'manage_polls', views.PollViewSet, basename='poll')
router.register(r'manage_questions', views.QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

for url in router.urls:
    print(url)
