# import spotipy
import requests
import base64
from pprint import pprint

CLIENT_ID = ""
CLIENT_SECRET =""
# client_creds = f"{client_id}:{client_secret}"
# client_creds_base64 = base64.b64encode(client_creds.encode())
# # Get a temporary token
TOKEN_URL = "https://accounts.spotify,com/api/token"
# method = "POST"
#
# token_data = {
#     "grant_type": "client_credentials"
# }
#
# token_headers = {
#     "Authorization": f"Basic {client_creds_base64.decode()}"
# }
#
# res = requests.post(token_url, data = token_data, headers = token_headers)
# pprint(res.json())


# SEARCH_URL = "https://api.spotify.com/v1/search";
# ARTIST_URL = "https://api.spotify.com/v1/artists/{}/top-tracks";

#basic auth that returns access token
def auth():
    data = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }

    res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
    res_data = res.json()

    access_token = res_data.get('access_token')
    return access_token

auth()