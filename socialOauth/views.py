import asyncio
from rest_framework.response import Response

from .github import Github
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from django.http import HttpResponseRedirect


class GithubRegisterAPI(GenericAPIView):
    def get(self, request):
        res = asyncio.run(Github.get_user_authorization())


class CallbackAPIView(GenericAPIView):
    """
    This endpoint receives the CODE and exchange it to a token
    """

    def get(self, request):
        code = request.query_params.get('code', None)
        data = asyncio.run(Github.request_access_token(code))
        access_token = data.get('access_token')
        user_email = asyncio.run(Github.get_user_email(access_token))
        user = Github.register_or_authenticate(
            user_email=user_email, access_token=access_token)
        tokens = user.get('tokens')
        refresh = tokens['refresh']
        access = tokens['access']

        # redirect
        REDIRECT_URL = 'http://localhost:3000/test'
        response = HttpResponseRedirect(REDIRECT_URL)
        response.set_cookie("refresh", refresh)
        response.set_cookie("access", access)
        return response


class TestView(GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        response = Response({'oh': f'you are authenticated {user.email}'})
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        response['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, PATCH, OPTIONS'
        return response
