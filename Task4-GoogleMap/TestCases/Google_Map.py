"""
Geo-Location application testing. Test the Google Map (https://www.google.com/maps) for:
a. Map loading
b. Zoom or pan controls
c. Searching for locations
d. Validation marker location of the fetched location
e. Search for route or direction between two locations
f. Validate the distance between the two locations of the fetched route
"""

from Map_Locators.Locators import Google_Map_Locators
from Map_Data.Data import GoogleMap_Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
#explicit wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re


class Homepage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait=WebDriverWait(self.driver,10)

    #Task-a:Load the map
    def start_automation(self):
        try:
            self.driver.get(GoogleMap_Data().url)
            self.driver.maximize_window()
            map_element = self.wait.until(EC.presence_of_element_located((By.XPATH,Google_Map_Locators().map_locator)))

            if map_element.is_displayed():
                print("Google map loaded Successfully")
                return True

            else:
                print("Unable to load the map")

        except WebDriverException as e:
            print("Invalid url", e)
            return False

    #Task-b:Zoom-in  and Zoom-out control
    def zoom(self):
        try:
            #zoom-in
            zoom_in_element=self.wait.until(EC.element_to_be_clickable((By.ID,Google_Map_Locators().Zoom_in_locator)))
            zoom_in_element.click()
            print("Zoomed_in Successfully")

            #zoom-out
            zoom_out_element=self.wait.until(EC.element_to_be_clickable((By.ID,Google_Map_Locators().zoom_out_locator)))
            self.driver.execute_script("arguments[0].click();", zoom_out_element)
            print("Zoomed out successfully")
            return True

        except NoSuchElementException as e:
            print("Unable to Zoom-In and Zoom-Out")
            return False

    #Task-c:Searching for locations
    def search_location(self):
        try:
            search_element = self.wait.until(EC.element_to_be_clickable((By.ID,Google_Map_Locators().search_box_locator)))
            search_element.clear()
            search_element.send_keys(GoogleMap_Data().search_data)
            search_element.send_keys(Keys.ENTER)
            print("Searching the location successfully")
            sleep(3)

            tittle_element = self.wait.until(EC.presence_of_element_located((By.XPATH,Google_Map_Locators().tittle_locator)))
            if tittle_element.is_displayed():
                print("Searched location is:", tittle_element.text)
                return True

            else:
                print("Unable to search location")

        except NoSuchElementException as e:
            print("Error", e)
            return False

    #Task-d: Validation marker location of the fetched location
    def marker_location(self):
        try:
            current_url = self.driver.current_url
            print("fetched location URL:", current_url)

            match = re.search(r'@([\d.-]+),([\d.-]+)', current_url)
            if match:
                lat, lng = float(match.group(1)), float(match.group(2))
                print(f"Marker location is: {lat},{lng}")

                if abs(lat - GoogleMap_Data().expected_lat) < 0.01 and abs(lng - GoogleMap_Data().expected_lng) < 0.01:
                    print("Marker is at the expected location")
                    return True

        except WebDriverException as e:
            print("Validation Failed", e)
            return False

    #task-e:Search for route or direction between two locations
    def direction(self):
        try:
            # click the direction button
            direction_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,Google_Map_Locators().direction_locator)))
            direction_element.click()
            print("successfully clicked the direction button")

            #enter the starting location
            start_location_element = self.wait.until(EC.presence_of_element_located((By.XPATH,Google_Map_Locators().start_location)))
            start_location_element.send_keys(GoogleMap_Data().start_location_data)
            start_location_element.send_keys(Keys.ENTER)
            #Enter the end location
            end_location_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,Google_Map_Locators().end_location)))
            end_location_element.clear()
            end_location_element.send_keys(GoogleMap_Data().end_location_data)
            end_location_element.send_keys(Keys.ENTER)
            print("Destination Route direction found successfully")
            #load the direction path im google map
            sleep(3)
            current_url = self.driver.current_url
            print("URL after Route search", current_url)

            if GoogleMap_Data().start in current_url and GoogleMap_Data().destination in current_url:
                print("Directions path loaded in the Google Map successfully")
                return True
            else:
                print("Directions not found")

        except NoSuchElementException as e:
            print("Unable to search direction between two locations")
            return False

    #Task-f: Validate the distance between the two locations of the fetched route
    def distance_validation(self):
        try:
            distance_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,Google_Map_Locators().distance_locator)))
            #distance validation
            if distance_element.is_displayed() and distance_element.is_enabled():
                distance = distance_element.text
                print("Distance fetched from the google map", distance)
                return True

        except NoSuchElementException as e:
            print("Unable to fetch the route distance", e)
            return False

    def shut_down(self):
        self.driver.quit()
        return None
