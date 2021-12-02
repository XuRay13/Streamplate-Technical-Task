from venue import Venue
from category import Category
from API import API
import datetime
import sys



class Answer:
    def __init__(self):

        self.project = API(49.000, -97.000, 5)    #API Object 
        self.project.process_data()



    def result(self):
        return self.project.get_categories()



    def print_all_categories(self):
        all_categories = self.project.categories

        print("ALL CATEGORIES:    (sorted)")
        for category in all_categories:       
            print(category["category"] + " = " + str(len(category["venues"])) + " venues"  ) 





start_time = datetime.datetime.now()




#ANSWER
x = Answer()
ans = x.result()
print("SORTED... ")
print()
for i in ans:
    print(i)
    print()


""" use to print all categories within limit in a readable form"""
#Prints all Categories
# x.print_all_categories()
# print()
# print()





end_time = datetime.datetime.now()
print(end_time - start_time)