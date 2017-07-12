#
# Example file for formatting time and date output
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now() # get the current date and time
    #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime(("%Y"))) #Full year with century
  print(now.strftime("%a,%d,%B,%y"))#Abbreviated day, num, full month, abbreviated year
if __name__ == "__main__":
  main();
