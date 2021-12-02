import math

class Category:
    def __init__(self, category_name):  
        self.category_name = category_name
        self.venues = []      
        self.num_venues = 0

    def add_venue(self, venue):
        self.venues.append(venue)
        self.num_venues += 1

    # Takes users current location and returns venues within distance limit ordered by nearest distance
    def get_venues_by_distance(self, current_location, limit):
        venues_distance = []
        for v in self.venues:
            
            venues_distance.append((v, calculate_distance(current_location, v.location)))

        venues_by_distance = sorted(venues_distance, key=lambda v: v[1])

        temp = venues_by_distance[:limit]
        self.num_venues = len(temp)
        return temp

        
    def details(self):
        print(self.category_name + ":  " + str(len(self.venues)) + " venues")
        for v in self.venues:
            print(v.name)

    
def calculate_distance(a, b):
    dist = math.sqrt((a.x - b.x)**2 + (a.y- b.y)**2)
    return dist


class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    


        