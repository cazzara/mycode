import turtle
import requests
import json
import time

def getISSPos():
    iss_loc_endpoint = 'http://api.open-notify.org/iss-now.json'
    resp = requests.get(iss_loc_endpoint)
    resp_json = json.loads(resp.text)
    loc = resp_json['iss_position']
    lat = loc['latitude']
    lon = loc['longitude']
    return lat, lon

def getISSNextPass(lat=47.660399, lon=-122.320479):
    iss_next_pass_sea = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(lat, lon)
    resp = requests.get(iss_next_pass_sea)
    resp_json = json.loads(resp.text)
    over = resp_json['response'][1]['risetime']
    return over

def drawMap(screen):
    screen.setup(720, 360) # set the resolution
    screen.setworldcoordinates(-180,-90,180,90)
    screen.bgpic('iss_map.gif')

def plotISSPos(lat, lon):
    screen.register_shape('spriteiss.gif')
    iss.shape('spriteiss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(round(float(lon)), round(float(lat)))

## My location
def plotMyPos(mylocation, lat=47.660399, lon=-122.320479):
    mylocation.penup()
    mylocation.color('yellow')
    mylocation.goto(round(float(lon)), round(float(lat)))
    mylocation.dot(5)
    mylocation.hideturtle()

def redrawISS(x, y):
    print("redrawing iss {} {}".format(x, y))
    iss_lat, iss_lon = getISSPos()
    plotISSPos(iss_lat, iss_lon)

def writePassTime(t, mylocation):
    style = ('Arial', 10, 'bold')
    mylocation.write(time.ctime(t), font=style)
    
if __name__ == "__main__":
    screen = turtle.Screen() # create a screen object
    iss = turtle.Turtle()    # create the ISS object
    turtle.onscreenclick(redrawISS)
    mylocation = turtle.Turtle() # create our position
    iss_lat, iss_lon = getISSPos()
    nextPassTime = getISSNextPass()
    drawMap(screen)
    plotISSPos(iss_lat, iss_lon)
    plotMyPos(mylocation)
    writePassTime(nextPassTime, mylocation)
    print("Click anywhere on the screen to update the ISS position")
    turtle.mainloop()
