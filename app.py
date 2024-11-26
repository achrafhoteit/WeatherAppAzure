from flask import Flask, request, render_template
from flask import jsonify # Needed for JavaScript
import requests

# Create an application referencing this file
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Javascript Version

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    api_key = "e4e1c78e2f0c5f2dbb1ab135e15eb74c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Unable to fetch weather data'}), 500
    
    data = response.json()
    return jsonify({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    })

# No JavaScript Version

# @app.route('/weather', methods=['POST'])
# def get_weather():
#     city = request.form.get('city') # Get city from form
#     api_key = "e4e1c78e2f0c5f2dbb1ab135e15eb74c"
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)

#     if response.status_code != 200:
#         return render_template('index.html', error="Unable to fetch weather data for the specified city.")
    
#     data = response.json()
#     weather = {
#         'city': data['name'],
#         'temperature': data['main']['temp'],
#         'humidity': data['main']['humidity'],
#         'description': data['weather'][0]['description']
#     }
#     return render_template('weather.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)