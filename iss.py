#!/usr/bin/env python

__author__ = 'Bethsheba Zebata'

import requests
import turtle
import urllib
import json
import time


def main():
    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    r = json.loads(response.read())
    print("Total # of astronauts in space: " + str(r["number"]) + "")

    people = r["people"]
    # print(people)

    for p in people:
        print(p["name"] + " is aboard " + p["craft"])

    # r_coord = requests.get('')
    # print(r_coord.text)

    t = turtle.Turtle()
    s = turtle.Screen()
    s.setup(800, 800)
    s.bgpic('map.gif')
    s.register_shape("iss.gif")
    s.setworldcoordinates(-180, -90, 180, 90)
    t.shape("iss.gif")
    t.setheading(45)
    t.penup()

    while True:
        url = 'http://api.open-notify.org/iss-now.json'
        response = urllib.request.urlopen(url)
        r = json.loads(response.read())
        location = r["iss_position"]
        lat = location["latitude"]
        lon = location["longitude"]

        print("Latitude: " + (lat))
        print("Longitude: " + (lon))

        t.goto(lon, lat)
        time.sleep(5)


if __name__ == '__main__':
    main()
