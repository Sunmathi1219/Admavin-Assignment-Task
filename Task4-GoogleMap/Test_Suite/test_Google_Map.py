"""
test_Google_Map.py file for generating Html report-Main executable file
"""

from TestCases.Google_Map import Homepage
from Map_Data.Data import GoogleMap_Data
import pytest

url = GoogleMap_Data().url
google_map = Homepage(url)


def test_map_loading():
    assert google_map.start_automation() == True


def test_zoom_control():
    assert google_map.zoom() == True


def test_search():
    assert google_map.search_location() == True


def test_marker_validation():
    assert google_map.marker_location() == True


def test_direction():
    assert google_map.direction() == True


def test_distance():
    assert google_map.distance_validation() == True

def test_close():
    assert google_map.shut_down() == None
    print("Google map test-cases automated successfully")
