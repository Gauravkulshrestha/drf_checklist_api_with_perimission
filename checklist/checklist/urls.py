from django.contrib import admin
from django.urls import path, include
from api.views import RegisterAPIView, LogOutAPIView, CheckListView, CheckListsView, CheckListItemAPIView,  CheckListItemCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/register/', RegisterAPIView.as_view(), name='register'),    
    path('api/logout/', LogOutAPIView.as_view(), name='logout'),    
    path('api/checklist/', CheckListView.as_view(), name='checklist'),    
    path('api/checklists/<int:pk>/', CheckListsView.as_view(), name='checklists'),
    path('api/checklistitem/create/', CheckListItemCreateAPIView.as_view(), name='cchecklists'),
    path('api/checklistitem/<int:pk>/', CheckListItemAPIView.as_view(), name='rudhecklists'),            
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]