import os
import aiohttp
import asyncio


class Github:
    """
    Github class to fetch the user info and return it
    """

    @staticmethod
    async def validate(access_token):
        """
        validate method of fetching data
        """
        headers = {
            "Authorization": f"token {access_token}",
            "content-type": "application/json",
        }
        try:
            async with aiohttp.ClientSession() as session:
                url = "https://api.github.com/user"
                async with await session.get(url, headers=headers) as res:
                    data = await res.json()
                    return data
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
                "code": code
            }
            headers = {
                "content-type": "application/json",
                "accept": "application/json",
            }
            async with session.post(url, headers=headers, params=params) as res:
                data = await res.json()
                return data
