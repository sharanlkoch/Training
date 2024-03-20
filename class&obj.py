#A class is a code template for creating objects

#Base class
class Learning:
    
    '''A FUNCTION is a block of code which only runs when it is called. 
    You can pass data, known as parameters, into a function. 
    A function can return data as a result.'''
    
    def learning(self):
        answer=str(input("What are currently working on? >>"))
        print("Currently I am working on " +answer)

#Child class using inheritance from Base class.    
class Progress(Learning):       
    
    def progress(self):
        answer1=str(input("What's the status on your learning? >>"))               
        print("Progress Status >> "+answer1)

#Another child class using concept of inheritance.    
class Mentor(Progress): 
       
    def mentor(self):
        answer2=str(input("Who is guiding you currently? >>"))
        if answer2=="Lakshay" or "Sunil":
            print("That's great!")
        else:
            print("That's Nice!")      

'''OBJECTS are variables that contain data and
functions that can be used to manipulate the data.'''

#Creating a object of the child class
my_training=Mentor()

#OOPs concept to access attributes and functions of a class.
#Using the objects we created, we can call the desired class.
my_training.learning()
my_training.progress()
my_training.mentor()

