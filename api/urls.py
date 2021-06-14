from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
urlpatterns = [
    path('social/', include('socialOauth.urls'), name='social'),
    path('auth/', include('authentication.urls'), name='auth'),

]
