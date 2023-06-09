# This is an example (using cURL syntax) of how to make a Spire Route Forecast API request.
# Please note that the "time", "lat", and "lon" values are ** not realistic ** in this example.
# It can be run from the terminal command-line using:
#
#       python python_example_request.py
#
# JSON response data can then be copy/paste/saved to a local file for further analysis.
# In the `convert_spire_json_to_csv.py` script, the JSON response data is expected to be
# in a local file called `spire_weather_data.json`.
# You can of course change the code if you would like to name the input file something different.
import pandas as pd
import requests
import json
from datetime import date
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import random

class moods:
    
    '''def getPlaylist():
        return playlist_url'''
    
    client_id = '6bae4451c248407d84e5808925840377'
    client_secret = '8d400f2e23ef4a27931e680fd9493db4'
    client_uri = 'http://localhost:8080/callback'

    scope = 'user-library-read playlist-modify-public'
    auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    user = sp.current_user()['id']

    # Define playlist categories
    high_energy_music = ['techno', 'house', 'hip hop', 'metal', 'rock']
    low_energy_music = ['blues', 'classical', 'instrumental']
    exciting_music = ['pop', 'dance', 'r&b', 'reggae', 'latin']
    depressed_music = ['r&b', 'ambient', ]


    @staticmethod
    def happyPlaylist():
        track_results = []
        client_id = '6bae4451c248407d84e5808925840377'
        client_secret = '8d400f2e23ef4a27931e680fd9493db4'
        client_uri = 'http://localhost:8080/callback'

        scope = 'user-library-read playlist-modify-public'
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        user = sp.current_user()['id']

        high_energy_music = ['techno', 'house', 'hip hop', 'metal', 'rock']
        for genre in high_energy_music:
            offset = random.randint(0, 100)
            results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
            for track in results['tracks']['items']:
                track_results.append(track['uri'])
        playlist = sp.user_playlist_create(user, name='Happy', public=True, description='Playlist of happiness')
        sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)
        playlist_url = playlist['external_urls']['spotify']
        print(playlist_url)
        return playlist_url

    @staticmethod
    def relaxationPlaylist():
        track_results = []
        client_id = '6bae4451c248407d84e5808925840377'
        client_secret = '8d400f2e23ef4a27931e680fd9493db4'
        client_uri = 'http://localhost:8080/callback'

        scope = 'user-library-read playlist-modify-public'
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        user = sp.current_user()['id']

        low_energy_music = ['blues', 'classical', 'instrumental']
        for genre in low_energy_music:
            offset = random.randint(0, 100)
            results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
            for track in results['tracks']['items']:
                track_results.append(track['uri'])
        playlist = sp.user_playlist_create(user, name='Relaxation', public=True, description='Playlist of relaxation')
        sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)
        playlist_url = playlist['external_urls']['spotify']
        print(playlist_url)
        return playlist_url

    @staticmethod
    def hypePlaylist():
        track_results = []
        client_id = '6bae4451c248407d84e5808925840377'
        client_secret = '8d400f2e23ef4a27931e680fd9493db4'
        client_uri = 'http://localhost:8080/callback'

        scope = 'user-library-read playlist-modify-public'
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        user = sp.current_user()['id']

        exciting_music = ['pop', 'dance', 'r&b', 'reggae', 'latin']
        for genre in exciting_music:
            offset = random.randint(0, 100)
            results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
            for track in results['tracks']['items']:
                track_results.append(track['uri'])
        playlist = sp.user_playlist_create(user, name='Hype', public=True, description='Playlist of hype music')
        sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)
        playlist_url = playlist['external_urls']['spotify']
        print(playlist_url)
        return playlist_url

    @staticmethod
    def depressedPlaylist():
        track_results = []
        client_id = '6bae4451c248407d84e5808925840377'
        client_secret = '8d400f2e23ef4a27931e680fd9493db4'
        client_uri = 'http://localhost:8080/callback'

        scope = 'user-library-read playlist-modify-public'
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        user = sp.current_user()['id']

        depressed_music = ['r&b', 'ambient', ]
        for genre in depressed_music:
            offset = random.randint(0, 100)
            results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
            for track in results['tracks']['items']:
                track_results.append(track['uri'])
        playlist = sp.user_playlist_create(user, name='Depressed', public=True, description='Playlist of depressing music')
        sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)
        
        playlist_url = playlist['external_urls']['spotify']
        print(playlist_url)
        return playlist_url
playlist_url = ""

class moodEval:

    url = "https://api.wx.spire.com/forecast/route"
    today = date.today()
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    input1 = str(today) + "T" + str(dt_string)


    zip = 95014
    def setZip(code):
        zip = code
    response = requests.get('https://thezipcodes.com/api/v1/search?zipCode=' + str(zip) + '&countryCode=US&apiKey=ded7388190c42055780b299ec6c41b14')
    json_string = response.text

    latIndex = json_string.find("latitude") + 11
    latitude = ""
    while(json_string[latIndex] != '"'):
        latitude += json_string[latIndex]
        latIndex += 1


    longIndex = json_string.find("longitude")  + 12
    longitude = ""
    while(json_string[longIndex] != '"'):
        longitude += json_string[longIndex]
        longIndex += 1

    #print(latitude, longitude) 
    #print(input1)

    payload = json.dumps(
        {
            "route": {
                "name": "my_example_route",
                "waypoints": [
                    {"time": input1, "lat": latitude, "lon": longitude},
                ],
            },
            "bundles": "basic,maritime",
        }
    )
    headers = {
        "spire-api-key": "DaVrozYhAZbbVJVb37AccvH8PjucQXTe",
        "Content-Type": "application/json",
    }
    response1 = requests.request("POST", url, headers=headers, data=payload)
    spire_string = response1.text
    windSpeedIndex = spire_string.find("wind_speed") + 12
    temperatureIndex = spire_string.find("air_temperature") + 17
    precipiationIndex = spire_string.find("precipitation_rate") + 20
    cloudCoverIndex = spire_string.find("total_cloud_cover") + 19
    humidityIndex = spire_string.find("relative_humidity") + 19
    wind_speed = ""
    air_temperature = ""
    precipitation_rate = ""
    total_cloud_cover = ""
    relative_humidity = ""
    #print(spire_string)
    while(spire_string[windSpeedIndex] != '}'):
        wind_speed += spire_string[windSpeedIndex]
        windSpeedIndex += 1
    while(spire_string[temperatureIndex] != ','):
        air_temperature += spire_string[temperatureIndex]
        temperatureIndex += 1
    while(spire_string[precipiationIndex] != ','):
        precipitation_rate += spire_string[precipiationIndex]
        precipiationIndex += 1
    while(spire_string[cloudCoverIndex] != ','):
        total_cloud_cover += spire_string[cloudCoverIndex]
        cloudCoverIndex += 1
    while(spire_string[humidityIndex] != ','):
        relative_humidity += spire_string[humidityIndex]
        humidityIndex += 1

    wind_speed = float(wind_speed)
    air_temperature = float(air_temperature)
    precipitation_rate = float(precipitation_rate)
    total_cloud_cover = float(total_cloud_cover)
    relative_humidity = float(relative_humidity)

    # print(response1.text)
    # print("Wind speed:",wind_speed)
    # print("temperature:", air_temperature)
    # print("precipitation:", precipitation_rate)
    # print("Cloud cover:", total_cloud_cover)
    # print("humidity:",relative_humidity)

    sleep = 4
    def setSleep(sleepGood):
        sleep = sleepGood
    health = 1
    def setHealth(goodHealth):
        health = goodHealth
    nostress = 4
    def setNostress(stress):
        nostress = stress
    celsius = air_temperature - 273.15
    print("total cloud cover " + str(total_cloud_cover))

    moodE = 0
    moodE += sleep * -0.007
    print("Your BioMood after sleep is " + str(moodE))
    moodE += health * -0.135
    print("Your BioMood after health is " + str(moodE))
    moodE += nostress * 0.177
    print("Your BioMood after nostress is " + str(moodE))
    moodE += celsius * 0.003
    print("Your BioMood after temp is " + str(moodE))
    moodE += relative_humidity * 0.002
    print("Your BioMood after humidity is " + str(moodE))
    moodE += wind_speed * 0.007
    print("Your BioMood after humidity is " + str(moodE))
    moodE += (1 - total_cloud_cover/100) * 0.095
    print("Your BioMood after sunshine is " + str(moodE))
    moodE += precipitation_rate * 0.007
    print("Your BioMood after rain is " + str(moodE))
    moodS = 0
    moodS += sleep * 0.029
    print("Your BioMood after sleep is " + str(moodS))
    moodS += health * 0.024
    print("Your BioMood after health is " + str(moodS))
    moodS += nostress * 0.190
    print("Your BioMood after nostress is " + str(moodS))
    moodS += celsius * -0.001
    print("Your BioMood after temp is " + str(moodS))
    moodS += relative_humidity * -0.0003
    print("Your BioMood after humidity is " + str(moodS))
    moodS += wind_speed * -0.000001
    print("Your BioMood after wind is " + str(moodS))
    moodS += (1 - total_cloud_cover/100) * 0.019
    print("Your BioMood after sunshine is " + str(moodS))
    moodS += precipitation_rate * 0.0005
    print("Your BioMood after rain is " + str(moodS))
    moodS *= 100
    moodE *= 100
    print("Energy mood is " + str(moodE) + " and sadness mood is " + str(moodS))
    if (moodE > 50): 
        if (moodE > 70): 
            #hype
            playlist_url = moods.hypePlaylist()
        else:
            #happy
            playlist_url = moods.happyPlaylist()
    else:
        if (moodE > 20):
            #relaxed
            playlist_url = moods.relaxationPlaylist()
            temp = ""
        else:
            #depressed
            playlist_url = moods.depressedPlaylist()
            temp = ""
@staticmethod
def getPlaylistUrl():
    return playlist_url