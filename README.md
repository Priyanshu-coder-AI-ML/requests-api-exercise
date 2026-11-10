# Requests and JSON Exercises

Five short Python exercises on working with web APIs using the [`requests`](https://requests.readthedocs.io) library and the built-in `json` module. They use the free test API [JSONPlaceholder](https://jsonplaceholder.typicode.com) (and [httpbin](https://httpbin.org) for headers).

## Project structure

```
requests-api-exercises/
├── src/
│   ├── task1_get_posts.py          # GET request, print first 5 titles
│   ├── task2_restaurant_json.py    # dict -> JSON string
│   ├── task3_post_request.py       # POST request with a JSON payload
│   ├── task4_query_params.py       # GET with ?userId=2
│   └── task5_custom_headers.py     # GET with custom headers
├── tests/
│   └── test_tasks.py               # offline tests (network is mocked)
├── .github/workflows/tests.yml     # runs the tests on every push
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

Requires Python 3.9 or newer.

```bash
git clone https://github.com/<your-username>/requests-api-exercises.git
cd requests-api-exercises

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the tasks

```bash
python src/task1_get_posts.py
python src/task2_restaurant_json.py
python src/task3_post_request.py
python src/task4_query_params.py
python src/task5_custom_headers.py
```

## What each task covers

### Task 1 - GET request
Calls `requests.get()` on `/posts`, parses the response with `.json()`, and prints the titles of the first 5 posts.
**Concepts:** GET, `raise_for_status()`, JSON parsing, list slicing, timeouts.

### Task 2 - Python dictionary to JSON
Builds a Zomato-style restaurant dictionary (name, location, cuisines, ratings, ...) and converts it with `json.dumps()`.
**Concepts:** nested dicts and lists, `json.dumps(indent=2)`, `None` becoming `null` and `True` becoming `true`, round-trip check with `json.loads()`.

### Task 3 - POST request
Sends a new "playlist" (`title`, `userId`, `body`) to `/posts` and prints the status code and JSON response.
**Concepts:** POST, the `json=` argument, status code `201 Created`.
**Note:** JSONPlaceholder only *simulates* writes. It replies with your data plus `"id": 101` but does not store it.

### Task 4 - Query parameters
Uses `params={"userId": 2}` so the request becomes `/posts?userId=2`, then prints the matching post IDs (11 to 20).
**Concepts:** the `params` argument, filtering on the server side.

### Task 5 - Custom headers
Sends a GET request with `Authorization`, `Accept`, `User-Agent` and a custom header via the `headers=` argument, and prints the status code. httpbin echoes the headers back so you can confirm they arrived.
**Concepts:** HTTP headers, Bearer tokens, keeping secrets out of source code.

To use a real token, set it as an environment variable instead of editing the code:

```bash
export API_TOKEN="your-real-token"     # Windows PowerShell: $env:API_TOKEN="your-real-token"
python src/task5_custom_headers.py
```

## Running the tests

The tests mock the network, so they work offline and in CI:

```bash
pytest -v
```

## Quick reference

| Goal | Code |
|------|------|
| GET | `requests.get(url, timeout=10)` |
| GET with query string | `requests.get(url, params={"userId": 2})` |
| POST JSON | `requests.post(url, json=data)` |
| Custom headers | `requests.get(url, headers={"Authorization": "Bearer TOKEN"})` |
| Check for errors | `response.raise_for_status()` |
| Read JSON | `response.json()` |
| Status code | `response.status_code` |

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Add requests and JSON exercises"
git branch -M main
git remote add origin https://github.com/<your-username>/requests-api-exercises.git
git push -u origin main
```
