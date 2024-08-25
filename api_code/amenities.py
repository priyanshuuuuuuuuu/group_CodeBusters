import requests

def find_nearest_police_stations(location, radius=5000):
    lat, lng = location['latitude'], location['longitude']
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node
      ["amenity"="police"]
      (around:{radius},{lat},{lng});
    out body;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    
    stations = [{
        'name': element.get('tags', {}).get('name', 'Unknown'),
        'lat': element['lat'],
        'lon': element['lon'],
        'distance': ((lat - element['lat'])**2 + (lng - element['lon'])**2) ** 0.5
    } for element in data['elements']]
    
    nearest_stations = sorted(stations, key=lambda x: x['distance'])[:5]
    return nearest_stations

def find_nearest_fire_stations(location, radius=5000):
    lat, lng = location['latitude'], location['longitude']
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node
      ["amenity"="fire_station"]
      (around:{radius},{lat},{lng});
    out body;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    
    stations = [{
        'name': element.get('tags', {}).get('name', 'Unknown'),
        'lat': element['lat'],
        'lon': element['lon'],
        'distance': ((lat - element['lat'])**2 + (lng - element['lon'])**2) ** 0.5
    } for element in data['elements']]
    
    nearest_stations = sorted(stations, key=lambda x: x['distance'])[:5]
    return nearest_stations

def find_nearest_hospital(location, radius=5000):
    lat, lng = location['latitude'], location['longitude']
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node
      ["amenity"="hospital"]
      (around:{radius},{lat},{lng});
    out body;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    
    stations = [{
        'name': element.get('tags', {}).get('name', 'Unknown'),
        'lat': element['lat'],
        'lon': element['lon'],
        'distance': ((lat - element['lat'])**2 + (lng - element['lon'])**2) ** 0.5
    } for element in data['elements']]
    
    nearest_stations = sorted(stations, key=lambda x: x['distance'])[:5]
    return nearest_stations
