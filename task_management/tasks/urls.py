from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskViewSet, TaskAssignViewSet, UserViewSet, UserTasksViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'assign_task', TaskAssignViewSet, basename='assign_task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/<int:user_id>/tasks/', UserTasksViewSet.as_view({'get': 'list'}), name='user_tasks'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get Access Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token
]
