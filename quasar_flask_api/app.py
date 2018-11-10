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
    # get timestamp which has seconds only as 00 or 10 or 20 or 30 or 40 or 50
    timestamp_datetime = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    correct_seconds = str(int(timestamp_datetime.second/10))+'0'
    timestamp = timestamp_datetime.strftime("%d.%m.%Y %H:%M:" + correct_seconds)
    
    # get corresponding value from our emulated database
    value = float((energy_ticker_data[timestamp]['value']).replace(' ', ''))
    
    response_dict = {"timestamp": timestamp, "value": value}
    response = json.dumps(response_dict)

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
