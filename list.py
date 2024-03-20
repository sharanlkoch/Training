'''LISTS are used to store multiple items in a single variable.
   Lists can be of different types
   List items are ordered, changeable, and allow duplicate values.(Mutable)
 '''
 
complex=[1,"Sharan",21130371,"Automation",["Sunil,Lakshay,Ravi"]]
print(complex)
#List constructor
this_list=list((1,"Sharan",21170731,"GP"))
print(this_list)

#Appending the items from list complex to this_list
for i in complex:
    if i not in this_list:
       this_list.append(i)

#Storing it in a new list
new_list=[]
for i in this_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)        


    


    