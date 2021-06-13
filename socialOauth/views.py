import asyncio

from .github import Github
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class CallbackAPIView(GenericAPIView):
    """
    This endpoint receives the CODE and exchange it to a token
    """

    def get(self, request):

        params = request.query_params
        code = params.get('code', None)
        if not code:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Code is necessary"})
        data = asyncio.run(Github.request_access_token(code))
        access = data.get('access_token')
        data = asyncio.run(Github.validate(access))

        return Response(data=data)
