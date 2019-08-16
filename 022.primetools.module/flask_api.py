from flask import Flask, json
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


def json_handler(func, desc, req, result, result_type):
    json_data = {
        "api_endpoint": func,
        "description" : desc,
        "request": req,
        "result_value": result,
        "result_type" : result_type
    }
    return json.dumps(json_data)

@api.route('/', methods=['GET'])
@api.route('/api/', methods=['GET'])
@api.route('/api/v1/', methods=['GET'])
def help():
    return help_text

@api.route('/api/v1/is_prime/<int:n>', methods=['GET'])
def get_is_prime(n):
    func = "is_prime"
    req = n
    result = pt.is_prime(n)
    desc = "Determines primality of a given integer."
    result_type = "boolean"
    return json_handler(func, desc, req, result, result_type)

@api.route('/api/v1/get_nth/<int:n>', methods=['GET'])
def get_nth_prime(n):
    func = "get_nth"
    desc = "Given a positive integer n, determines n-th prime number"
    req = n
    result = pt.get_nth(n)
    result_type = "integer"
    return json_handler(func, desc, req, result, result_type)

@api.route('/api/v1/nearest/<int:n>', methods=['GET'])
def get_nearest_prime(n):
    func = "nearest"
    desc = "Returns the nearest prime number to a given integer."
    req = n
    result = pt.get_nearest(n)[0]
    result_type = "integer"
    return json_handler(func, desc, req, result, result_type)

@api.route('/api/v1/neighbors/<int:n>', methods=['GET'])
def get_prime_neighbors(n):
    func = "neighbors"
    desc = "Given an integer n, returns the greatest prime which is less than n and the smallest prime which is greater than n."
    req = n
    result = pt.get_neighbors(n)
    result_type = "array"
    return json_handler(func, desc, req, result, result_type)

@api.route('/api/v1/factorize/<int:n>', methods=['GET'])
def get_prime_factors(n):
    func = "factorize"
    desc = "Returns the prime factors of a given integer."
    req = n
    result = pt.factorize(n)
    result_type = "array"
    return json_handler(func, desc, req, result, result_type)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=deploy_port)
