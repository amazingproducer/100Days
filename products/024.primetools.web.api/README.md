## Note:
# PrimeTools Web API
This application utilizes the PrimeTools portable module to provide web endpoints for each of its prime number calculations, including:
- Primality Evaluation
- n-th Prime Calculation
- Find nearest prime number(s)
- Prime Factorization

## Usage:
_While it is possible to clone the entire 100days repository and run a local copy of the PrimeTools web API, evaluating the [auto-deployed heroku instance](https://prime-tools.herokuapp.com/api/v1) is recommended._

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


PrimeTools Module
-----------------

### Functions

`factorize(n)`
:   Calculates prime factors of n. Returns a list.


`generate()`
:   Generator Function. Yields successive prime numbers.


`get_nearest(n, y=1)`
:   Calculates the prime number which the lowest difference from n. Returns
    an integer.


`get_neighbors(n)`
:   Calculates the greatest prime number which is less than n and the lowest
    prime number which is greater than n. Returns list.


`get_nth(n)`
:   Determines the n-th prime number. Returns an integer.


`get_ordinal(n)`
:   Determines the proper ordinal for an integer n. Returns a string.


`is_prime(n)`
:   Determines primality of n. Returns boolean.

