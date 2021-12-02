
#   1  - process data
#read file
#for each venue/line:
    #categories = {} 
    #venues = {}

    #create Venue() Object
    
    #for each of Venues() categories:
        #check if Category Object already exists in categories
            #if not:
                #create Category() object 
                #create keyValue pair. {Venue.name: Venue.address}
                #add(keyValue pair) to Category.venues
                
                #add categories[Category.name] = CategoryObject
                #add venues[Venue.name] = VenueObject


            #else:
                #get Category() object
                #create keyValue pair for Venue. {Venue.name: Venue.address}
                #add(keyValue pair) to Category().venues

                #re-add into categories.  categories[Category.name] = CategoryObject]

            #add Venue() to venues.  venues[Venue.name] = Venue()


#  2  - sort
#sort each Category based on number of venues it has
#store in list

#  3  - return to API
#for each Category in sorted list:
    #create keyValue pair.  {Category.name: Category.venues}
    #add to self.categories



import math
import datetime
from venue import Venue
from category import Category
import sys
from Location import Location



class API:
    def __init__(self, latitude, longitude, limit=10):
        self.current_location = Location(float(latitude), float(longitude))
        self.limit = limit
        
        self.categories = []  #Return Variable
        self.file = sys.argv[1]

        self.all_categories = {} #{"American": Object(American),  "Asian": Oject(American)}
        self.all_venues = {}


    def get_categories(self):
        return self.categories




    def process_data(self):
        #1   Process data into necessary Object instances
        try:
            file = open(self.file, "r")
            file.readline().strip("\n")  # name,address,categories,latitude,longitude
        except FileNotFoundError:
            print("File doesn't exist !!")
            exit()


        while True:
            line = file.readline().strip("\n")    #read each line
            if line == "":
                break
            
            split = line.split(',')
            latitude = split[-2]
            longitude = split[-1]
        
            split = line.split('"') 
            name = split[1]
            address = split[3]

            location = Location(float(latitude), float(longitude))

            try:
                file_categories = split[5]
                split_categories = file_categories.split(",")
            except IndexError:
                split_categories = []


            #Create Venue Object
            venue = Venue(name, address, split_categories, location)
            self.all_venues[venue.name] = venue


            #Find Category or Create
            for c in venue.categories:
                #category exists
                if c in self.all_categories.keys():
                    category = self.all_categories[c]
                    category.add_venue(venue)
                    self.all_categories[category.category_name] = category

                #category doesn't exist
                else:
                    category = Category(c)
                    category.add_venue(venue)
                    self.all_categories[category.category_name] = category
                


        #2 sort all_categories and limit venues
        self.categories = self.get_nearest_venues_by_categories()


    def get_nearest_venues_by_categories(self):
        # sort venues by distance
        # filter by limit distance
        # group by sorted categories
        # return result
        
        categories = []

        for key in self.all_categories:
            venues_by_distance = self.all_categories[key].get_venues_by_distance(self.current_location, self.limit)
            categories.append({
                "category": self.all_categories[key].category_name,
                "venues": [{
                    "name": v[0].name, 
                    "address": v[0].address
                } for v in venues_by_distance]
            })

        result = sorted(categories, key = lambda c: c["category"])
        result = sorted(result, key=lambda c: len(c["venues"]), reverse=True)
        
        return result




def calculate_distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist













 



