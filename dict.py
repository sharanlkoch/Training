import datetime
import os
#To read the output in dict format
from pprint import pprint

#ec2 instance dict from boto3 documentation
ec2_instance={
    'Reservations': [
        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'sharan'
                },
            ],
            'Instances': [
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': 'string',
                    'InstanceType':'dk',
                    'KernelId': 'string',
                    'KeyName': 'string',
                }   
                    
            ],
            'OwnerId': 'string',
            'RequesterId': 'string',
            'ReservationId': 'string'
        },
    ],
    'NextToken': 'string'
}

#Function to find the value of the describe      
def find(obj,filename):
    answer=None
    #Checking if the described value is in key-value pairs
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'GroupId':
                answer= value
            else:
                answer = find(value,filename)
                if answer is not None:
                    break
    #If value not in Dict, Checks in list            
    elif isinstance(obj, list):
        for item in obj:
            answer = find(item,filename)
            if answer is not None:
                break
    if answer is not None:
        with open(filename,'w')as file:
            file.write(answer)
    return answer        

#Assiging the result to a variable.
find(ec2_instance,'Answer.txt')


'''
with open('Answer.txt','r')as file:
    content=file.read()
    print(content)
'''
filename='Answer.txt'
if os.path.exists(filename):
    os.system(f'start {filename}')
else:
    print("File does not exist!")    


       
            