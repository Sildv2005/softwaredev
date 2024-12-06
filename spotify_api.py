import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "96d2ceceda184977804830832ef4d0a9"
CLIENT_SECRET = "7c4d8bfad2c746a09a63201e8f2652ec"
REDIRECT_URI = "http://localhost:8080/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read"
))

results = sp.current_user_saved_tracks(limit=10)
for idx, item in enumerate(results["items"]):
    track = item["track"]
print(f"{idx + 1}: {track['name']} van {track['artists'][0]['name']}")
