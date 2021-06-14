import asyncio

from .github import Github
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


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

        return Response(data=user)
