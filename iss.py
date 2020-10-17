#!/usr/bin/env python

__author__ = 'Bethsheba Zebata'


import turtle
import urllib.request
import json
import time


def indy():
    url = 'http://api.open-notify.org/iss-pass.json?lat=39.7&lon=86.1&alt=20&n=5'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    time_passed = result["response"]
    for t in time_passed:
        datetime = time.ctime(t['risetime'])
        print("ISS will be over Indy on  " + datetime)


def main():
    indy()
    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print("Total # of astronauts in space: " + str(result["number"]) + "")

    people = result["people"]

    for p in people:
        print(p["name"] + " is aboard " + p["craft"])

    s = turtle.Screen()
    s.setup(720, 360)
    s.setworldcoordinates(-180, -90, 180, 90)
    s.bgpic('map.gif')
    s.register_shape("iss.gif")

    t = turtle.Turtle()
    t2 = turtle.Turtle()
    t.shape("iss.gif")
    t2.shape("circle")
    t2.color('yellow')
    t.setheading(45)
    t.penup()

    while True:
        url = 'http://api.open-notify.org/iss-now.json'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        location = result["iss_position"]
        lat = location["latitude"]
        lon = location["longitude"]

        print("Latitude: " + str(lat))
        print("Longitude: " + str(lon))
        print("time: " + str(time.ctime(result['timestamp'])))

        t.goto(float(lon), float(lat))
        time.sleep(5)


if __name__ == '__main__':
    main()
