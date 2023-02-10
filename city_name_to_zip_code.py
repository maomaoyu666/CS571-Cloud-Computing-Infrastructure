from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/zipcode/<state_name>/<city_name>")
def get_zip_code(state_name, city_name):
	result = requests.get(f'https://api.zippopotam.us/us/{state_name}/{city_name}').json()

	zip_codes = [place['post code'] for place in result['places']]
	zip_code = zip_codes[0]
	weather_url = f"http://127.0.0.1:8080/weather/{zip_code}"

	weather_res = requests.get(weather_url)
	if weather_res.status_code == 200:
		return f"{weather_res.text}"
	else:
		return f"Request failed with status code: {weather_res.status_code}"

if __name__ == "__main__":
	app.run(debug=True, port=5050)