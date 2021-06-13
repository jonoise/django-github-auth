- [] have a basic understanding of JWT
- [] get the code
  - [x] update callback in github
  - [] implement callback in backend
    - [x] callback receive a code
    - [x] get parameters code/state
    - [] validate state
    - [x] exchange code for access token to post https://github.com/login/oauth/access_token with
- [] get state
- [] verify IF state.exists()
- [x] exchange code for access_token
- [x] POST https://github.com/login/oauth/access_token
- [x] client_id string Required. The client ID for your GitHub App.
- [x] client_secret string Required. The client secret for your GitHub App.
- [x] code string Required. The code you received as a response to Step 1.

### RESPONSE:

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

# Your GitHub App accesses the API with the user's access token

The user's access token allows the GitHub App to make requests to the API on behalf of a user.

```shell
Authorization: token OAUTH-TOKEN
GET https://api.github.com/user
```
