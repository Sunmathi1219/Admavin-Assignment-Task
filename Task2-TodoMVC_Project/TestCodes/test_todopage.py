"""
test_todopage.py
Main executable file
"""


import pytest

from Data.TodoPageData import TodoPage
from Locators.TodoPageLocators import Todo_locators

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
#explicit wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_TodoTask:
    @pytest.fixture
    def booting(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait=WebDriverWait(self.driver,10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_add_tasks(self,booting):
        try:

            #Task1-open the application in browser

            self.driver.get(TodoPage().url)

            assert self.driver.current_url == TodoPage().url
            print("success")

            #Task2-Add 3 tasks with different name

            textbox_element=self.wait.until(EC.presence_of_element_located((By.ID,Todo_locators().textbox_locator)))

            #Add multiple tasks
            for task in TodoPage().tasks:
                textbox_element.send_keys(task)
                textbox_element.send_keys(Keys.ENTER)

            added_tasks_element=self.wait.until(EC.presence_of_element_located((By.XPATH,Todo_locators().added_tasks_locator)))
            if added_tasks_element.is_displayed():
                added_tasks = added_tasks_element.text

                assert added_tasks == TodoPage().added_tasks
                print("Added items Message displayed successfully :",added_tasks)


            #Task3-Mark the second task as complete

            checkbox_element=self.wait.until(EC.presence_of_element_located((By.XPATH,Todo_locators().checkbox_locator)))
            self.driver.execute_script("arguments[0].click()", checkbox_element)

            complete_element=self.wait.until(EC.presence_of_element_located((By.XPATH,Todo_locators().complete_locator)))
            if complete_element.is_displayed():
                completed_task=complete_element.get_attribute("class")
                assert completed_task == TodoPage().task2_completed
                print("Successfully mark the task as completed:",completed_task)


            #Task-4 Delete the first task

            item1_element=self.wait.until(EC.presence_of_element_located((By.XPATH,Todo_locators().task1_locator)))
            actions=ActionChains(self.driver)
            actions.move_to_element(item1_element).perform()

            delete_button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,Todo_locators().delete_button_locator)))
            delete_button.click()

            items_left_element=self.wait.until(EC.presence_of_element_located((By.XPATH,Todo_locators().items_left_locator)))
            if items_left_element.is_displayed():
                final_items=items_left_element.text
                assert final_items == TodoPage().final_items_left
                print("Successfully deleted the first task:",final_items)


        except NoSuchElementException as e:
            print("Error-Unable to do task",e)





