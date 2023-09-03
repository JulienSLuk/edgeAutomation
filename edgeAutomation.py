from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import concurrent.futures
import csv

# Function to check if a webpage is up after logging in
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

# Method to read data from a CSV file and optionally skip the first row
def read_csv(filename, skip_header=True):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)  # Skip the first row (header)
        for row in reader:
            data.append(row)
    return data

# Read data from CSV files with headers skipped for some
links = read_csv('links.csv')
driver_paths = read_csv('driver_paths.csv')
credentials = read_csv('credentials.csv', skip_header=True)

# Check multiple links concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(check_page, links, [c[0] for c in credentials], [c[1] for c in credentials], driver_paths)

# Print results
for link, title in results:
    print(f"Link: {link} - Page Title: {title}")
