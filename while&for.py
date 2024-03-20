'''WHILE LOOPS to run the same task multiple times
   and FOR LOOPS to loop once over list data.'''


print("Enter names of the members in GP DBA Team")
#Empty list to append the names entered by user.
names=[]
#Initializing the size of the list
user_input=5
#Using for loop to append members serially
for i in range(user_input):
    members=str(input())
    names.append(members)
    print(names)
    continue

#Using While loop to traverse over the list 
print("Members in the GP DBA Team")
size=len(names)
i=0
while(i<size):
    print(names[i])
    i+=1
        
    
    