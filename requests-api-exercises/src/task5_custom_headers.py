"""Task 5: Send a GET request with custom HTTP headers (e.g. Authorization)."""

import os

import requests

# httpbin.org echoes back whatever you send, which makes it ideal for testing headers.
API_URL = "https://httpbin.org/headers"

# Never hard-code real secrets in a repo. Read the token from an environment variable.
API_TOKEN = os.getenv("API_TOKEN", "demo-token-123")


def build_headers(token):
    return {
        "Authorization": f"Bearer {token}",   # common scheme for token-based APIs
        "Accept": "application/json",
        "User-Agent": "requests-api-exercises/1.0",
        "X-Custom-Header": "hello-from-python",
    }


def fetch_with_headers(token=API_TOKEN):
    response = requests.get(API_URL, headers=build_headers(token), timeout=10)
    return response


def main():
    try:
        response = fetch_with_headers()
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    print("Status code:", response.status_code)

    # Optional: show that the server received our custom headers.
    received = response.json().get("headers", {})
    print("Server saw X-Custom-Header:", received.get("X-Custom-Header"))


if __name__ == "__main__":
    main()
