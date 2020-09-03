"""django imports."""
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()
router.register('users', views.UserListApi, basename='usersviewset')

urlpatterns = router.urls
