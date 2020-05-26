import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'Access Token'
secret = 'Secret Token'

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_credentials_manager = SpotifyClientCredentials(client_id=cid,
client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
