from flask import Flask, jsonify, json
import PrimeTools as pt
import os
import requests


deploy_port = int(os.environ.get('PORT', 5000))
callback_url = str(os.environ.get('PT_DEV_CALLBACK'))

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


def send_response(route, desc, request, result_value, result_type):
    """Reusable function for spitting out the fancy JSON."""
    return jsonify(
        api_endpoint=route,
        description=desc,
        request=request,
        result_value=result_value,
        result_type=result_type
    )


@api.route('/', methods=['GET'])
@api.route('/api/', methods=['GET'])
@api.route('/api/v1/', methods=['GET'])
def help():
    """Print the ugly, manually-written route list."""
    return help_text


@api.route('/error_heroku.json', methods=['GET'])
def error_heroku():
    return jsonify(
        error="Operation timed out."
    )


@api.route('/api/v1/is_prime/<n>', methods=['GET'])
def get_is_prime(n):
    route = "is_prime"
    description = "Determines primality of a given integer."
    if not str(n).isdigit() or int(n) < 1:
        return send_response(route, description,  n, "Input must be a natural \
number.", "Error")
    if int(n) > 1000:
        report = "```CALLBACK - " + \
            str(n)+" primality: "+str(pt.is_prime(int(n))) + \
                ". I am not a ninja.```"
        requests.post(callback_url, json={
                      "content": report, "username": "tensus"})
        return send_response(route, description, n, "Available via \
callback URL.", "callback")
    return send_response(route, description, n, pt.is_prime(int(n)),
                          "boolean")


@api.route('/api/v1/get_nth/<n>', methods=['GET'])
def get_nth_prime(n):
    route = "get_nth_prime"
    description = "Given a positive integer n, determine the n-th prime number."
    if not str(n).isdigit() or int(n) < 1:
        return send_response(route, description, n, "Input must be a natural \
number.", "Entry")
    if int(n) > 1000:
        report = "```CALLBACK - n-th prime where n=" + \
            str(n)+": "+str(pt.get_nth(int(n)))+".```"
        requests.post(callback_url, json={
                      "content": report, "username": "tensus"})
        return send_response(route, description, n, "Available via callback \
URL.", "callback")
    return send_response(route, description, n, pt.get_nth(int(n)), "integer")


@api.route('/api/v1/nearest/<n>', methods=['GET'])
def get_nearest_prime(n):
    route = "get_nearest"
    description = "Returns the nearest prime number to a given integer."
    if not str(n).isdigit() or int(n) < 1:
        return send_response(route, description, n, "Input must be a natural \
number.", "Error")
    return send_response(route, description, n, pt.get_nearest(int(n))[0], "integer")

@api.route('/api/v1/neighbors/<n>', methods = ['GET'])
def get_prime_neighbors(n):
    route="neighbors"
    description="Given an integer n, returns the greatest prime which is \
less than n and the smallest prime which is greater than n."
    if not str(n).isdigit() or int(n) < 1:
        return send_response(route, description, n, "Input must be a natural \
number.", "Error")
    if int(n) < 3:
        return send_response(route, description, n, "Input must be greater \
than 2.", "Error")
    return send_response(route, description, n, pt.get_neighbors(int(n)),
"array")

@api.route('/api/v1/factorize/<n>', methods=['GET'])
def get_prime_factors(n):
    route = "factorize"
    description = "Returns the prime factors of a given integer."
    if not str(n).isdigit() or int(n) <= 1:
        return send_response(route, description, n, "Input integer must be \
greater than one.", "Error")
    return send_response(route, description, n, pt.factorize(int(n)), "array")

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=deploy_port)
