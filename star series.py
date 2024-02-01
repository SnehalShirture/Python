#1
# for i in range (1,6):
#     for j in range (1,6):
#         print ("*",end=" ")
#     print()

# #2
# for i in range (1,6):
#     for j in range (1,6):
#         print ("1",end=" ")
#     print()

#3
# for i in range (1,5):
#     for j in range (1,2):
#         print ("1","2","3","4",end="  ")
        
#     print() 


#5
# for i in range (1,5):
#     for j in range (1,4):
        
#         print (i,end=" ")
#     print()

#6
# for i in range (1,5):
#     for j in range (3,0,-1):
        
#         print (j,end=" ")
#     print()

# #7
# for i in range (3,0,-1):
#     for j in range (1,4):
#          print (i,end=" ")
#     print()
    

# #8
# for i in range (1,):
#     for j in range (5,0,-1):
#          print (i,end=" ")
#     print()

# #9
# for i in range (1,5):
#     for j in range (1,i+1):
#         print ("*",end =" ")
#     print()

# #10
# for i in range (1,5):
#     for j in range (1,i+1):
#         print (i,end =" ")
#     print()

# #11
# for i in range (1,6):
#     for j in range (1,i+1):
#         if (i%2==0):
#             print ("*",end =" ")
#         else :
#             print (i,end =" ")
#     print()

# #12
# for i in range (1,6):
#     for j in range (1,i+1):
        
#         if (i%2==0):
#             print (j,end =" ")
#         else :
#             print ("*",end =" ")
#     print()

# #13

# for i in range (1,6):
#     for j in range (1,5-i):
       
#             print ("*",end =" ")
        
#     print()
#         #OR
# for i in range (3,0,-1):
#     for j in range (1,i+1):
       
#             print ("*",end =" ")
        
#     print()


#   LINEAR SEARCH
# def linear(li,ele):
#     size = len(li)
#     for i in range (0,size):
#         if (li[i]== ele):
#             return i
#         else:
#             return -1

# li=[10,20,30,40]
# ele=int(input("enter the element to be search " ))
# index = linear(li,ele)
# if(index == -1):
#     print("element not found")
# else :
#     print("element found at index number ", index)




# #   BINARY SEARCH 
# def binary(data, ele):
#     beg = 0
#     end = len(data) - 1
#     while beg <= end:
#         mid = (beg + end) // 2
#         if ele == data[mid]:
#             return mid 
#         elif ele > data[mid]:
#             beg = mid + 1
#         else:
#             end = mid - 1
#     else:
#         return -1

# data = [1, 4, 7, 8, 12, 15, 27]
# ele = int(input("enter the number "))
# index = binary(data, ele)
# if index == -1:
#     print("element not found")
# else:
#     print("element found at", index)

#   SELECTION SORTING 
# data=[40,30,11,22,44,55,3]
# n=len(data)
# for i in range (0,n):
#     min = data[i]
#     index=i
#     for j in range (i+1,n):
#         if (min>data[j]):
#             min=data[j]
#             index=j
#     data [i],data [index]= data[index],data[i]
# print ("Sorted array is ", data)


# # FIND THE MINIMUM AND MAXIMUM NUMBER 

# data=[40,50,10,30,24,8,14]
# max = data [0]
# min = data [0]
# n=len (data)
# for i in range (1,n):
#     if (max<data[i]):
#         max = data[i]
#     if (min>data[i]):
#         min=data[i]
# print ("maximum number is ",max)
# print("maximum number is ", min)




import random
import requests
from bs4 import BeautifulSoup
from linkedin_api import Linkedin

def automate_linkedin_connections(competitor_profile_url, username, password):
    linkedin = Linkedin(username, password)
    
    response = requests.get(competitor_profile_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        decision_makers = soup.select('.decision-maker-class')
        
        for decision_maker in decision_makers:
            decision_maker_url = decision_maker['href']
            connections = scrape_connections(decision_maker_url)
            
            for connection in connections:
                analyzed_connection = analyze_profile_data(connection)
                if analyzed_connection:
                    personalized_message = generate_personalized_message(analyzed_connection)
                    send_connection_request(linkedin, analyzed_connection['profile_url'], personalized_message)

def scrape_connections(profile_url):
    response = requests.get(profile_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        connection_elements = soup.select('.connection-class')
        
        connections = []
        for connection_element in connection_elements:
            connection_name = connection_element.select_one('.name-class').text.strip()
            connection_info = {
                'name': connection_name,
                'profile_url': connection_element['href']
            }
            
            connections.append(connection_info)
        
        return connections
    else:
        return []

def analyze_profile_data(connection):
    response = requests.get(connection['profile_url'])
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        about_section = soup.select_one('.about-section-class')
        about_text = about_section.text.strip() if about_section else ''
        job_description = soup.select_one('.job-description-class')
        job_description_text = job_description.text.strip() if job_description else ''
        
        connection['about'] = about_text
        connection['job_description'] = job_description_text
        
        return connection
    else:
        return None

def generate_personalized_message(connection):
    message_templates = [
        f"Hey {connection['name']}, let's connect and explore synergies!",
        f"Hi {connection['name']}, I'm interested in connecting with you.",
        f"Hello {connection['name']}, let's expand our professional network.",
    ]
    
    personalized_message = random.choice(message_templates)
    return personalized_message

def send_connection_request(linkedin, profile_url, personalized_message):
    result = linkedin.invite_to_network(profile_url=profile_url, message=personalized_message)
    if result:
        print("Connection request sent")
    else:
        print("Failed to send connection request")

# Example usage
competitor_profile_url = 'https://www.linkedin.com/company/competitor'
username = 'your_linkedin_username'
password = 'your_linkedin_password'

automate_linkedin_connections(competitor_profile_url, username, password)


