"""django imports."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views


router = DefaultRouter()  # trailing_slash=False
router.register('activity', views.ActivityApi, basename='activityapi')
router.register('activitystatus', views.ActivityStateApi,
                basename='activitystatusapi')
router.register('useractivity', views.ActivityTrackerApi,
                basename='useractivityapi')
router.register('client', views.ClientApi, basename='clientapi')
router.register('system', views.SystemApi, basename='systemapi')

urlpatterns = [
    path('', include(router.urls)),
]
