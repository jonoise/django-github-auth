import os
import aiohttp
from django.contrib.auth import authenticate
from authentication.models import MainUser


class Github:
    """
    Github class to fetch the user info and return it
    """

    @staticmethod
    async def get_user_authorization():
        headers = {
            "content-type": "application/json",
            "Access-Control-Expose-Headers": "ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval"
        }
        async with aiohttp.ClientSession() as session:
            url = "https://github.com/login/oauth/authorize"
            async with await session.get(url, headers=headers) as res:
                data = await res.json()
                return data

    @staticmethod
    async def get_user_email(access_token):
        """
        validate method of fetching data
        """
        headers = {
            "Authorization": f"token {access_token}",
            "content-type": "application/json",
            "Access-Control-Expose-Headers": "ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval"
        }
        try:
            async with aiohttp.ClientSession() as session:
                url = "https://api.github.com/user/emails"
                async with await session.get(url, headers=headers) as res:
                    data = await res.json()
                    # El return es el email en formato string.
                    return data[0].get('email')
        except:
            return {"message": "The token is invalid or expired."}

    @staticmethod
    async def request_access_token(code):
        GITHUB_ID = os.environ.get('GITHUB_ID')
        GITHUB_SECRET = os.environ.get('GITHUB_SECRET')
        async with aiohttp.ClientSession() as session:
            url = "https://github.com/login/oauth/access_token"
            params = {
                "client_id": GITHUB_ID,
                "client_secret": GITHUB_SECRET,
                "code": code,
            }
            headers = {
                "content-type": "application/json",
                "accept": "application/json",
                "Access-Control-Expose-Headers": "ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval"
            }
            async with session.post(url, headers=headers, params=params) as res:
                data = await res.json()
                return data

    @staticmethod
    def register_or_authenticate(user_email, access_token):

        registered_user = MainUser.objects.filter(email=user_email).first()

        if registered_user:
            authenticated_user = authenticate(
                email=registered_user.email, password=os.environ.get('GITHUB_SECRET_PASSWORD'))

            return {
                "message": "user logged in",
                'id': authenticated_user.pk,
                'tokens': authenticated_user.tokens(),
            }

        newUser = MainUser.objects.create_user(
            email=user_email, password=os.environ.get('GITHUB_SECRET_PASSWORD'))
        newUser.github_access_token = access_token
        newUser.provider = 'github'
        newUser.save()

        authenticated_user = authenticate(
            email=newUser.email, password=os.environ.get('GITHUB_SECRET_PASSWORD'))

        return {
            'id': authenticated_user.pk,
            'tokens': authenticated_user.tokens(),
        }
