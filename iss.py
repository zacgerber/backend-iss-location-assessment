
import json
import turtle
import urllib.request
# import requests
import time


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)

result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'] + ', Craft: ' + str(p['craft']))


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])

print('Latitude: ', lat)
print('Longitude: ', lon)


new_lat = float(lat)
new_lon = float(lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/map.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

screen.register_shape(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/iss.gif')
iss = turtle.Turtle()
iss.shape(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(new_lon, new_lat)

# Space Center, Houston
# lat = float(29.5502)
# lon = float(-95.097)
url = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# Indianapolis
lat = 39.768452
lon = -86.156212
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()
over = result['response'][1]['risetime']
time.ctime(over)
style = ('Arial', 12, 'normal')
location.write(over, align='center', font=style)

if screen is not None:
    print('Click on screen to exit ...')
    screen.exitonclick()

# url = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
# response = urllib.request.urlopen(url)
# result = json.loads(response.read())
# response = requests.get(url).read()
# response = urllib.request.urlopen(url)
# result = json.loads(response.rea())
# location.goto(lon, lat)
# location.dot(5)
# location.hideturtle()
# over = result['response'][1]['risetime']
# style = ('Arial', 12, 'normal')
# location.write(time.ctime(over, font=style))
