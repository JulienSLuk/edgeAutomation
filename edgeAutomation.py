from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import concurrent.futures
import csv

# Function to check if webpage is up after logging in
def check_page(link, username, password, driver_path):
    driver = webdriver.Edge(executable_path=driver_path)
    driver.get(link)
    
    # Log in
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    submit_button = driver.find_element_by_id("submit")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    
    # You can implement further checks to verify if the login was successful
    
    time.sleep(3)  # Allow time for the page to load
    page_title = driver.title
    
    driver.quit()
    
    return link, page_title

# Read data from CSV files
links = []
driver_paths = []
usernames = []
passwords = []

with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row[0])

with open('driver_paths.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        driver_paths.append(row[0])

with open('usernames.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        usernames.append(row[0])

with open('passwords.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        passwords.append(row[0])

# Check multiple links concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(check_page, links, usernames, passwords, driver_paths)

# Print results
for link, title in results:
    print(f"Link: {link} - Page Title: {title}")
