# functions to create campus events at random
# Both linked list and array implementation can call this script

class Event:
    def __init__(self, id, title, date, time, location):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.location = location


# Create a unique ID
import random

def unique_ID():
