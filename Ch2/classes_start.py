#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
#Making a class with two methods
class myclass():
    def method1(self):
        print("Hello")
    def method2(self,mystring): #self argument is automatic and points to the object itself
        print("HELLO"+mystring)
      
def main():
    c=myclass()
    c.method1()
    c.method2("Neeraj")
  
if __name__ == "__main__":
  main()
