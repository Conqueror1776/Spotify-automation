import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'Access Token'
secret = 'Secret Token'

def connect_api(client_id, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spotify = connect_api(cid, secret)
