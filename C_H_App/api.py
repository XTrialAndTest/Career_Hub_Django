from . import views
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobs', Jobviewsets, basename='job')
router.register(r'company', Company_viewsets, basename='company')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    # path('job', views.job, name='job'),
]
