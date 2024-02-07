from geopy.geocoders import Nominatim
import geocoder
import datetime

def get_location_name(latitude, longitude):
    geolocator = Nominatim(user_agent="myGeoCoder")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address


def get_location():
    g = geocoder.ip('me')
    return g.latlng

def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None


