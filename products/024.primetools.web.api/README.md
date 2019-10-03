# PrimeTools Web API
This application utilizes the PrimeTools portable module to provide web endpoints for each of its prime number calculations, including:
- Primality Evaluation
- n-th Prime Calculation
- Find nearest prime number(s)
- Prime Factorization

## HTML Documentation
[PrimeTools Web API](https://prime-tools.shamacon.us/docs/flask_api.html)
[PrimeTools CLI and Module](https://prime-tools.shamacon.us/docs/PrimeTools.html)

## Usage:
_While it is possible to use a sparse checkout and run a local copy of the PrimeTools web API, evaluating the automatically deployed instance at https://prime-tools.shamacon.us/api/v1 is recommended._

### Endpoints:
HTTP Method	| Route				| Feature
--------------- | ----------------------------- | ----------
GET		| /api/v1/is_prime/{INTEGER}	| determine the primality of an integer
GET		| /api/v1/get_nth/{INTEGER}	| calculate the n-th prime number
GET		| /api/v1/nearest/{INTEGER}	| find an integer's nearest prime
GET		| /api/v1/neighbors/{INTEGER}	| find an integer's nearest neighboring primes
GET		| /api/v1/factorize/{INTEGER}	| calculate prime factors of an integer

### As a Command Line app:
```
usage: PrimeTools.py [-h] [-p P] [-n N] [--nearest NEAREST]
                     [--neighbors NEIGHBORS] [-f FACTORIZE] [-v]

PrimeTools Python Module - a part of 2019 100 Days of Coding

optional arguments:
  -h, --help            show this help message and exit
  -p P                  determine primality (default)
  -n N                  calculate n-th prime number
  --nearest NEAREST     calculate nearest prime number
  --neighbors NEIGHBORS
                        calculate neighboring prime numbers
  -f FACTORIZE, --factorize FACTORIZE
                        calculate prime factors
  -v                    Increase output verbosity
```
