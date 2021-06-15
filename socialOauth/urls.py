from django.urls import path
from .views import CallbackAPIView, TestView
app_name = "social"

urlpatterns = [
    # path('register/github/', GithubRegisterAPI.as_view(), name="github-register"),
    # path('frontend', FrontEndHandler.as_view(), name="frontend-request"),
    path('test/', TestView.as_view(), name="test"),
    path('callback/github/', CallbackAPIView.as_view(), name="callback"),
]
