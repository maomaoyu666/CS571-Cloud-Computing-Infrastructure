from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/weather/<zip_code>") 
def get_weather(zip_code):
    #zip_code = request.form['zipcode'] 
    api_key = "cccaa51ddda68ae37d30739d8ea596b9"
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}'
    weather_data = requests.get(weather_url).json()
    if "error" in weather_data:
        return jsonify({"error": weather_data["error"]}), 400

    location = weather_data["location"]
    current = weather_data["current"]   

    return jsonify({
        "location": location["name"],
        "region": location["region"],
        "country": location["country"],
        "temp_c": current["temp_c"],
        "condition": current["condition"]["text"],
        "icon": current["condition"]["icon"],
    })
    

if __name__ == "__main__":
    app.run(debug=True, port=8080)