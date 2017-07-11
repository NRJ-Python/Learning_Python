#
# Example file for working with loops
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x = 0
  #While Loop
  while(x<5):
      print(x)
      x=x+1
  #For Loop
  for x in range(5,10):
      print(x)
  #Using Loop over a collection
  days=["Mon","Tue","Wed"]
  for x in days:
      print(x)    
  #Using Break and Continue
  for x in range(5,10):
      if(x==7):break
      print(x) #Print 5 and 6 only
  for x in range(5,10):
      if(x%2==0):continue
      print(x) #Skips even number            
if __name__ == "__main__":
  main()
