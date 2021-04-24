from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="https://nominatim.openstreetmap.org/ui/search.html")
location = geolocator.geocode(input("enter location: "))
print("Address:", location.address)
print(("Latitude:", location.latitude, "Longitude:", location.longitude))
#print(location.raw)
print("Point:", location.point)
