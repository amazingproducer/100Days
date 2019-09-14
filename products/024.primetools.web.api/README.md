## Note:
# PrimeTools Web API
This application utilizes the PrimeTools portable module to provide web endpoints for each of its prime number calculations, including:
- Primality Evaluation
- n-th Prime Calculation
- Find nearest prime number(s)
- Prime Factorization

## Usage:
_While it is possible to clone the entire 100days repository and run a local copy of the PrimeTools web API, evaluating the live [heroku deployment](https://prime-tools.herokuapp.com/api/v1) is recommended._

### Endpoints:
HTTP Method	| Route				| Feature
--------------- | ----------------------------- | ----------
GET		| /api/v1/is_prime/{INTEGER}	| determine the primality of an integer
GET		| /api/v1/get_nth/{INTEGER}	| calculate the n-th prime number
GET		| /api/v1/nearest/{INTEGER}	| find an integer's nearest prime
GET		| /api/v1/neighbors/{INTEGER}	| find an integer's nearest neighboring primes
GET		| /api/v1/factorize/{INTEGER}	| calculate prime factors of an integer

