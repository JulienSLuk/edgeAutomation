from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import concurrent.futures

# Define your links
links = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]
username = "your_username"
password = "your_password"

# Function to check if webpage is up after logging in
def check_page(link):
    driver = webdriver.Edge(executable_path='path_to_edge_driver')  # Specify the path to your Edge webdriver executable
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

# Check multiple links concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(check_page, links)

# Print results
for link, title in results:
    print(f"Link: {link} - Page Title: {title}")
