"""django imports."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()  # trailing_slash=False
router.register('users', views.UserListApi, basename='usersviewset')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginAPI.as_view()),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
