
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
lat = float(location['latitude'])
lon = float(location['longitude'])
timestamp = result['timestamp']

print('Latitude: ', lat)
print('Longitude: ', lon)


earth = "map.gif"
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic(earth)

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
screen.exitonclick()
iss.goto(lon, lat)


# Indianapolis
# lat = 39.768452
# lon = -86.156212

# Space Center, Houston
# lat = 29.5502
# lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'https://spotthestation.nasa.gov/tracking_map.cfm' + str(float(lat))
+ '&lon=' + str(float(lon))
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

over = result['response'][1]['risetime']
style = ('Ariel', 6, 'bold')
location.write(time.ctime(over), font=style)
# print(over)


if screen is not None:
    screen.exitonclick()
