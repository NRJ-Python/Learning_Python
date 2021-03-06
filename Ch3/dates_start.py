#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime
def main():
#Date Objects
#Get today's date from today() method from date class
 today=date.today()
 print("Today's date is :",today)
 #Print out date's individual components
 print("Date Components :",today.day,today.month,today.year) 
 #Retrieve today's weekday (0=Monday , 6=Sunday)
 print("Today's weekday is",today.weekday())
 #Get today's date and time from datetime class
 today=datetime.now()
 print("The date and time is :",today)
 #Get the current time
 t=datetime.time(datetime.now())
 print("The current time is :",t)
 #Getting day number and day
 wd=date.weekday(today)
 print("Today's day number is %d" % wd)
 day=["Mon", "Tue" ,"Wed"]
 print("And the days is ",day[wd])
if __name__ == "__main__":
  main();
  