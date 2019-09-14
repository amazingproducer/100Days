## Note:
# PrimeTools Web API
This application utilizes the PrimeTools portable module to provide web endpoints for each of its prime number calculations, including:
- Primality Evaluation
- n-th Prime Calculation
- Prime number Generator Function
- Find nearest prime number(s)
- Prime Factorization

## Usage:
_While it is possible to clone the entire 100days repository and run a local copy of the PrimeTools web API, evaluating the live [heroku deployment](https://prime-tools.herokuapp.com/api/v1) is recommended._

### Endpoints:
HTTP Method	| Route
--------------- | --------------------------
GET		| /api/v1/is_prime/{INTEGER}
GET		| /api/v1/get_nth/{INTEGER}
GET		| /api/v1/nearest/{INTEGER}
GET		| /api/v1/neighbors/{INTEGER}
GET		| /api/v1/factorize/{INTEGER}


