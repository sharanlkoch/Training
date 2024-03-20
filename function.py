#Creating a base class
class interning():

    #__init__ is an instance method that initializes a newly created object.
    
    ''' SELF represents the instance of class.
    This handy keyword allows you to access variables,
    attributes, and methods of a defined class in Python.'''
    
    def __init__(self):
        print('  Welcome to DBA Team -KOCH')
    
    #User-driven function
    def function1(self):
        print("    Choose your interest")
        answer=str(input("Administration || Automation \n"))
        if answer=="Administration":
            print("You will be learning SQL Server!")
        elif answer=="Automation":
            print("You will be learning Python and SQL Server!")
        else:
            print("Enter a valid input")    

        
    def function2(self):
        print("  So what did you choose?")
        answer1=str(input("Administration || Automation \n"))
        
        if answer1=="Administration":
            print("Ravi will be guiding you :)")
        elif answer1=="Automation":
            print("Sunil and Lakshay will be guiding you :)")    
    
    #Simple function using multiple if-else statements.        
    def multipleif(self):
        user_input=int(input("Enter a value either 1 || 0 \n"))
        if user_input==1 or 0:
            if user_input==1:
                print("Value is high")
            else:
                print("Value is low")
        else:
            print("Enter valid input :)")         

#Create an object of the class intering()        
sharan=interning()

#Calling the functions using the object we created.
sharan.function1()            
sharan.function2()
sharan.multipleif()
         