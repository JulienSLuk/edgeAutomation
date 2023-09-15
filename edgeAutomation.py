from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import concurrent.futures
import csv
from selenium.webdriver.edge.service import Service

# Function to check if a webpage is up after logging in
def check_page(edge_driver_path, link, username_id, password_id, login_id, username, password):
    # WebDriver services
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.get(link)
    
    # Log in
    username_field = driver.find_element(By.ID, username_id)
    password_field = driver.find_element(By.ID, password_id)
    submit_button = driver.find_element(By.ID, login_id)
    
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
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Read data from CSV files with headers skipped for some
edge_driver_path = read_csv('driver_paths.csv', skip_header=True)
info_data = read_csv('info.csv', skip_header=True)

# Check multiple links concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(lambda info: check_page(
        edge_driver_path[0]['path'],
        info['link'],
        info['username_id'],
        info['password_id'],
        info['login_id'],
        info['username'],
        info['password']
    ), info_data)

# Print results
for link, title in results:
    print(f"Link: {link} - Page Title: {title}")
