""""
Todo page locators
"""

class Todo_locators:
    #task2 locator
    textbox_locator="todo-input"
    todo_items_locator="//ul[@class='todo-list']//li//div//label"
    added_tasks_locator="//footer[@class='footer']//span"
    #task3 locator
    checkbox_locator="//main[@class='main']//ul[@class='todo-list']//li[2]//div//input[@type='checkbox']"
    complete_locator="//ul[@class='todo-list']//li[2][@class='completed']"
    task2_completed = "completed"
    #task4 locator
    task1_locator="//ul[@class='todo-list']//li[1]"
    delete_button_locator="destroy"
    items_left_locator="//footer[@class='footer']//span"

