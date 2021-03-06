from flask import Flask, jsonify, json
import PrimeTools as pt
import os

deploy_port = int(os.environ.get('PORT', 5000))

api = Flask(__name__)

help_text = """
<h3>PrimeTools Web API:</h3>
<table style="width:100%">
  <tr>
  <th style="text-align:left">HTTP Method</th>
  <th style="text-align:left">Route</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/is_prime/{INTEGER}</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/get_nth/{INTEGER}</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/nearest/{INTEGER}</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/neighbors/{INTEGER}</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/v1/factorize/{INTEGER}</td>
  </tr>
</table>
"""

@api.route('/', methods=['GET'])
@api.route('/api/', methods=['GET'])
@api.route('/api/v1/', methods=['GET'])
def help():
    return help_text

@api.route('/api/v1/is_prime/<int:n>', methods=['GET'])
def get_is_prime(n):
    return jsonify(
        api_endpoint = "is_prime",
        description = "Determines primality of a given integer.",
        request = n,
        result_value = pt.is_prime(n),
        result_type = "boolean"
    )

@api.route('/api/v1/get_nth/<int:n>', methods=['GET'])
def get_nth_prime(n):
    return jsonify(
        api_endpoint = "get_nth",
        description = "Given a positive integer n, determines n-th prime number",
        request = n,
        result_value = pt.get_nth(n),
        result_type = "integer",
    )

@api.route('/api/v1/nearest/<int:n>', methods=['GET'])
def get_nearest_prime(n):
    return jsonify(
        api_endpoint = "nearest",
        description = "Returns the nearest prime number to a given integer.",
        request = n,
        result_value = pt.get_nearest(n)[0],
        result_type = "integer"
    )

@api.route('/api/v1/neighbors/<int:n>', methods=['GET'])
def get_prime_neighbors(n):
    return jsonify(
        api_endpoint = "neighbors",
        description = "Given an integer n, returns the greatest prime which is less than n and the smallest prime which is greater than n.",
        request = n,
        result_value = pt.get_neighbors(n),
        result_type = "array"
    )

@api.route('/api/v1/factorize/<int:n>', methods=['GET'])
def get_prime_factors(n):
    return jsonify(
        api_endpoint = "factorize",
        description = "Returns the prime factors of a given integer.",
        request = n,
        result_value = pt.factorize(n),
        result_type = "array"
    )

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=deploy_port)
