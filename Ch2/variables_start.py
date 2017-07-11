# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
#Declare a variable and initialize it
f=0;
print(f)
#Re-Declare a variable
f="abc"
print(f)
#Error :Different types can't be combined
#print("string")+123 [Gives Error]
print("string" +str(123))
def somefunction():
    global f
    f="def"
    print(f) #Gives output = def
somefunction()
print(f) #Gives output =def
del (f) # Delete a variable
print (f) # Gives error as f is deleted