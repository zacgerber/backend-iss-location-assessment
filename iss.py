
import json
import turtle
import time
import urllib.request
import requests

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'] + ', Craft: ' + str(p['craft']))

url1 = requests.get('http://api.open-notify.org/iss-now.json')
iss_time = url1.json()['timestamp']
location = url1.json()['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])

print('Latitude: ', lat)
print('Longitude: ', lon)

new_lat = float(lat)
new_lon = float(lon)

url = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
response = requests.get(url)
response.raise_for_status()

screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic('map.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(new_lon, new_lat)
iss.color('yellow')

# time stamp for iss
over = response.json()['response'][1]['risetime']
style = ('Arial', 12, 'bold')
iss.write(time.ctime(iss_time), font=style)

# Space Center, Houston
# lat = float(29.5502)
# lon = float(-95.097)

url = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
response = requests.get(url)
response.raise_for_status()

# Indianapolis
lat = 39.768452
lon = -86.156212
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()
over = response.json()['response'][1]['risetime']
style = ('Arial', 12, 'normal')
location.write(time.ctime(over), align='center', font=style)

if screen is not None:
    print('Click on screen to exit ...')
    screen.exitonclick()
