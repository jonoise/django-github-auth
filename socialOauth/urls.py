from django.urls import path
from .views import CallbackAPIView
app_name = "social"

urlpatterns = [
    path('callback/github/', CallbackAPIView.as_view(), name="callback")
]
