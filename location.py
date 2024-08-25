import requests

def get_current_location():
    try:
        ip_info = requests.get('https://ipinfo.io').json()
        location = ip_info['loc'].split(',')
        return {
            'latitude': float(location[0]),
            'longitude': float(location[1]),
        }
    except Exception as e:
        print(f"Error retrieving location: {e}")
        return None
