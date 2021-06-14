from django.urls import path
from .views import CallbackAPIView
app_name = "social"

urlpatterns = [
    # path('register/github/', GithubRegisterAPI.as_view(), name="github-register"),
    # path('frontend', FrontEndHandler.as_view(), name="frontend-request"),
    path('callback/github/', CallbackAPIView.as_view(), name="callback"),
]
