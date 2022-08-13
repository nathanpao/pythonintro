from datetime import *

class Event:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = []

    def addVenue(self, venue):
        self.venue.append(venue)

class Venue:
    def __init__(self, name):
        self.name = name
        self.address = []

    def addAddress(self, address):
        self.address.append(address)

class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

event = Event(date(2022, 1, 1), date(2023, 1, 1))
venue = Venue("Broadway Theater")
address = Address("123 Street", "Manhattan", "New York", "America", 12345)
venue.addAddress(address)
event.addVenue(venue)

print(event.startTime)
print(event.endTime)
for eachVenue in event.venue:
    print(eachVenue.name)
    for eachAddress in venue.address:
        print(eachAddress.street)
        print(eachAddress.city)
        print(eachAddress.state)
        print(eachAddress.country)
        print(eachAddress.zipcode)