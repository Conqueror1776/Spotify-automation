import spotipy

# Connect to Spotify API
def connect_api(filename):
    filecache = read_client(filename)
    cid = filecache['client_id']
    secret = filecache['secret_token']
    username = filecache['username']
    return spotipy.util.prompt_for_user_token(username, "playlist-modify-public user-library-read", cid, secret, "http://127.0.0.1:9090")

# Get Tokens and username from file
def read_client(filename):
    filecache = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split()
            filecache[key] = val
    return filecache

# Returns a list of the first 50 liked songs
def get_liked_songs(spotify):
    return spotify.current_user_saved_tracks()

# Compares the liked songs to the json file and adds those which are not present
def write_liked_songs(songs):
    #TODO
    return null

# Analyzes a song based on the K_clustering algorithm and adds it to the specified playlist
def analyze_song(song):
    ## TODO
    return nulll

# Adds the song to the specified playlist
def add_song(song, playlist):
    # TODO
    return null
