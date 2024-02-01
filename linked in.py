
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