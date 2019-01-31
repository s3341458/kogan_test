from api import calculate_aircon_cubic_weight_avg
from flask import Flask, jsonify
from flask_cors import cross_origin

host = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
endpoint = '/api/products/1'

app = Flask(__name__)


@app.route('/')
@cross_origin()
def index():
    average_weight = calculate_aircon_cubic_weight_avg(
        {'host': host, 'endpoint': endpoint}
    )
    return jsonify({'averageWeight': "{}kg".format(average_weight)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
