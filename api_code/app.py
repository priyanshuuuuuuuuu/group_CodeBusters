from flask import Flask, render_template
import json
from location import get_current_location
from amenities import find_nearest_police_stations, find_nearest_fire_stations, find_nearest_hospital

app = Flask(__name__)

def get_amenities():
    location = get_current_location()
    police_stations = find_nearest_police_stations(location)
    fire_stations = find_nearest_fire_stations(location)
    hospitals = find_nearest_hospital(location)
    
    return {
        'location': location,
        'police_stations': police_stations,
        'fire_stations': fire_stations,
        'hospitals': hospitals
    }

@app.route('/')
def login():
    return render_template('loginPage.html')

@app.route('/main')
def home():
    return render_template('main/index.html')

@app.route('/about')
def about():
    return render_template('About/index.html')

@app.route('/griveance')
def griveance():
    return render_template('complain/index.html')
@app.route('/map')
def index():
    amenities = get_amenities()
    return render_template('map.html', amenities=json.dumps(amenities))

if __name__ == '__main__':
    app.run(debug=True)
