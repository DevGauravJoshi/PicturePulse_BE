from django.urls import path

from . import views

from rest_framework_simplejwt.views import ( TokenRefreshView)

urlpatterns = [
    path('user/', views.getUser.as_view(), name="User"),
    path('userinfo/', views.getUserInfo.as_view(), name="UserInfo"),
    path('usermedia/', views.getMedia.as_view(), name="usermedia"),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]
