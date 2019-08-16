from flask import Flask, json
import PrimeTools as pt

api = Flask(__name__)

help_text = """
PrimeTools Web API:
<br>
Method  Route
<br>
GET     /prime/api/v1/is_prime/{INTEGER}
<br>
GET     /prime/api/v1/get_nth/{INTEGER}
<br>
GET     /prime/api/v1/nearest/{INTEGER}
<br>
GET     /prime/api/v1/neighbors/{INTEGER}
<br>
GET     /prime/api/v1/factorize/{INTEGER}
"""

@api.route('/prime', methods=['GET'])
@api.route('/prime/api/', methods=['GET'])
@api.route('/prime/api/v1/', methods=['GET'])
def help():
    return help_text

@api.route('/prime/api/v1/is_prime/<int:n>', methods=['GET'])
def get_is_prime(n):
    return str(pt.is_prime(n))

@api.route('/prime/api/v1/get_nth/<int:n>', methods=['GET'])
def get_nth_prime(n):
    return str(pt.get_nth(n))

@api.route('/prime/api/v1/nearest/<int:n>', methods=['GET'])
def get_nearest_prime(n):
    return str(pt.get_nearest(n))

@api.route('/prime/api/v1/neighbors/<int:n>', methods=['GET'])
def get_prime_neighbors(n):
    return str(pt.get_neighbors(n))

@api.route('/prime/api/v1/factorize/<int:n>', methods=['GET'])
def get_prime_factors(n):
    return str(pt.factorize(n))

if __name__ == '__main__':
    api.run(host='0.0.0.0')
