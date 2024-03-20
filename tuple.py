'''
    TUPLES are immutable.This makes them ideal 
    for storing data that should not be modified, 
    such as database records.
'''
#Format to create a tuple
members=("Ravi","Praveen","Praveen","Lakshay","Sunil","Akshay","Jaideep","Keerthi","Sharan")
#Tuple Constructor
tuple_constructor=tuple(("Ravi","Praveen","Praveen","Lakshay","Sunil","Akshay","Jaideep","Keerthi","Sharan"))

#Traversing through the tuple and used if-elif statements.
for i in members:
    if i=="Ravi":
        print("Ravi is my supervisor")
    elif i=="Lakshay":
        print("Lakshay is my mentor")  
    else:
        print(i)
          
        
    
    