from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('social/', include('socialOauth.urls'), name='socialOauth')
]
