# sensorhub
import sensorhub

# other stuff
import logging
from flask import Flask, send_file, request, Response
from prometheus_client import start_http_server, Gauge, generate_latest

# initialize the sensorhub
I2C_ADDR = 26 # 0x1a
sensorhub = sensorhub.SensorHub(I2C_ADDR)

# PROMETHEUS FLASK SERVER
logger = logging.getLogger(__name__)

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

# create metrics to track sensor data
SENSORHUB_NOISELEVEL = Gauge(
    'sensorhub_noiselevel_db',
    'Noise level observed by the Sensor Hub'
)

# configure the metrics endpoint
@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""
    try:
        SENSORHUB_NOISELEVEL.set(sensorhub.recvBytes())
    except Exception as e:
        logger.error("Failed to update noise level. Exception: {}".format(e))
    
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# run the web server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# BASIC FLASK SERVER
# app = Flask(__name__)

# @app.route('/')
# def getSensorDataJson():
#     sensorData = {
#         "Noise Level": "%0.1f dB" % sensorhub.recvBytes()
#     }
#     return json.dumps(sensorData)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9100)