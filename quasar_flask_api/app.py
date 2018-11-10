from flask import Flask
import datetime
import json
import pytz

# Load Flask application
app = Flask(__name__)

# Load energy ticker database into memory
with open('energy_ticker_data.json', 'r') as f:
    energy_ticker_data_json = f.read()
energy_ticker_data = json.loads(energy_ticker_data_json)

@app.route("/")
def hello():
    return "<h1>Energy ticker API</h1><br>" +\
           "Check <a href=\"/energy_ticker/get_tick\">/energy_ticker/get_tick</a> " +\
           "to get energy ticker data"

@app.route("/energy_ticker/get_tick")
def funcname():
    timestamp = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%Y %H:%M:00")
    value = float((energy_ticker_data[timestamp][0]['value']).replace(' ', ''))
    
    response_dict = {"timestamp": timestamp, "value": value}
    response = json.dumps(response_dict)

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
