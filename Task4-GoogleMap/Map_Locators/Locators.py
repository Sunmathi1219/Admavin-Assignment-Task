"""
locators for google map tasks
"""


class Google_Map_Locators:
    #map loading
    map_locator = "//div[@class='id-content-container']//div[1]//div[3]//canvas[1]"
    #zoom control
    Zoom_in_locator = "widget-zoom-in"
    zoom_out_locator = "widget-zoom-out"
    #searching
    search_box_locator = "searchboxinput"
    tittle_locator = "//div[@class='TIHn2 ']//div//div//div//h1[contains(@class,'DUwDvf lfPIob')]"
    #direction path
    direction_locator = "//button[@data-value='Directions']"
    start_location = "//div[@id='directions-searchbox-0']//input[@class='tactile-searchbox-input']"
    end_location = "//div[@id='directions-searchbox-1']//div//div//input"
    route_locator = "//div[contains(text(),'min')]"
    distance_locator = "ivN21e"
