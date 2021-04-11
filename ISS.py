import json
import turtle
import urllib.request
import time
import geocoder


print('****************************************')
print('************* ISS LOCATOR **************')
print('****************************************')

people_url = "http://api.open-notify.org/astros.json"   # URL for open notify API
response = urllib.request.urlopen(people_url)             # gets URL
result = json.loads(response.read())                    # loads json file from API

no_people = result["number"]                            # gets number of people from json
print(f'\nThere are {no_people} people on board the ISS')    # outputs number of people
people = result["people"]                               # gets list of people from json file
print('Onboard ISS:')
for x in people:                                        # for each person prints name
    print(x['name'])
    time.sleep(2)                                       # waits before output next name

place = geocoder.ip('me')                                   # gets location of user
print("Your current latitude and Longitude is " + str(place.latlng))  # outputs to user

print('\n-CONFIG-')

time_input = True
while time_input:
    try:
        time_user = int(input('Enter Refresh time (Seconds) for coordinates \n'))  # user enters refresh rate
        if 5 >= time_user >= 1:                         # compares with range
            time_input = False                          # if in range ends loop
        else:
            raise ValueError                            # if value not in range, raises error
    except ValueError:
        print('Enter between 1-5')                      # handles error and outputs instruction to user, loop continues


screen = turtle.Screen()                                # creates screen for turtle
screen.setup(1280, 720)                                 # sets area of screen
screen.setworldcoordinates(-180, -90, 180, 90)          # sets coordinates for turtle


screen.bgpic("map.gif")                     # load the world map image
screen.register_shape("iss.gif")            # gets ISS image
iss = turtle.Turtle()                       # sets ISS as turtle
iss.shape("iss.gif")
iss.setheading(45)                          # sets heading for turtle
iss.penup()                                 # prevents turtle draw

while True:
    url = "http://api.open-notify.org/iss-now.json"          # opens URL for current location
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())                # loads json file
    location = result["iss_position"]                   # Extract the ISS location
    lat = location['latitude']                          # sets variable to latitude
    lon = location['longitude']                         # sets variable longitude

    lat = float(lat)                                    # converts to float
    lon = float(lon)                                    # converts to float

    print('')
    print('ISS Status')
    print("Current Latitude: " + str(lat))            # outputs latitude as string
    print("Current Longitude: " + str(lon))           # outputs longitude as string

    try:
        iss.goto(lon, lat)                            # update the ISS location on the map
    except Exception:                                 # handles when window is closed by user
        print('window closed')
        break                                         # halts loop
    time.sleep(time_user)                             # waits for refresh time to restart loop

