
import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)

result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

print('Latitude: ', lat)
print('Longitude: ', lon)

new_lat = float(lat)
new_lon = float(lon)

screen = turtle.Screen()

screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/iss.gif')
screen.bgpic(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/map.gif')

# screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape(
    '/Users/zacgerber/zacs-quarter3/backend-iss-location-assessment/iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(new_lon, new_lat)


# Indianapolis
lat = float(39.768452)
lon = float(-86.156212)

# Space Center, Houston
# lat = float(29.5502)
# lon = float(-95.097)

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()
screen.exitonclick()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat)
+ '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# print(result)

over = result['response'][1]['risetime']
location.write(time.ctime(over))
