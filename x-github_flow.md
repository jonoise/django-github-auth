# Web application flow

Using the web application flow, the process to identify users on your site is:

1. Users are redirected to request their GitHub identity
2. Users are redirected back to your site by GitHub
3. Your GitHub App accesses the API with the user's access token

# 1. Request a user's GitHub identity

USEFULL RESOURCES

- GET https://github.com/login/oauth/authorize
- client_id=Iv1.c32838396cb342b5
- https://github.com/login/oauth/authorize?client_id=Iv1.c32838396cb342b5&status=234as24-sd5gq5-e5r4h-qa5s4d5

### Parameters

| Name         | Type   | Description                                                                                                                                                                                                                         |
| ------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client_id    | string | Required. The client ID for your GitHub App. You can find this in your GitHub App settings when you select your app. Note: The app ID and client ID are not the same, and are not interchangeable.                                  |
| redirect_url | string | he URL in your application where users will be sent after authorization. This must be an exact match to one of the URLs you provided as a Callback URL when setting up your GitHub App and can't contain any additional parameters. |
| state        | string | This should contain a random string to protect against forgery attacks and could contain any other arbitrary data.                                                                                                                  |
| login        | string | Suggests a specific account to use for signing in and authorizing the app.                                                                                                                                                          |
| allow_signup | string | Whether or not unauthenticated users will be offered an option to sign up for GitHub during the OAuth flow. The default is true. Use false when a policy prohibits signups.                                                         |

# 2. Users are redirected back to your site by GitHub

If the user accepts your request, GitHub redirects back to your site with a temporary code in a code parameter as well as the state you provided in the previous step in a state parameter. If the states don't match, the request was created by a third party and the process should be aborted.

**Exchange this code for an access token.** to this url https://github.com/login/oauth/access_token via POST. With the following params.

| Name          | Type   | Description  |
| ------------- | ------ | ------------ |
| client_id     | string | **Required** |
| client_secret | string | **Required** |
| code          | string | **Required** |

### RESPONSE:

By default, the response takes the following form. The response parameters expires_in, refresh_token, and refresh_token_expires_in are only returned when you enable expiring user-to-server access tokens.

```JSON
{
  "access_token": "ghu_16C7e42F292c6912E7710c838347Ae178B4a",
  "expires_in": 28800,
  "refresh_token": "ghr_1B4a2e77838347a7E420ce178F2E7c6912E169246c34E1ccbF66C46812d16D5B1A9Dc86A1498",
  "refresh_token_expires_in": 15811200,
  "scope": "",
  "token_type": "bearer"
}
```

# 3. Your GitHub App accesses the API with the user's access token

The user's access token allows the GitHub App to make requests to the API on behalf of a user.

```shell
Authorization: token OAUTH-TOKEN
GET https://api.github.com/user
```

```shell
curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com/user
```
