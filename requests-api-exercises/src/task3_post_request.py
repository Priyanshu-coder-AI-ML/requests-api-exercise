"""Task 3: Send a POST request to add a new playlist (JSON payload)."""

import json

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

new_playlist = {
    "title": "Late Night Coding Mix",
    "userId": 1,
    "body": "Lo-fi beats and instrumental tracks for focused programming sessions.",
}


def create_playlist(payload):
    """POST the payload as JSON and return the response object."""
    # `json=` serialises the dict and sets Content-Type: application/json for us.
    response = requests.post(API_URL, json=payload, timeout=10)
    response.raise_for_status()
    return response


def main():
    try:
        response = create_playlist(new_playlist)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    print("Status code:", response.status_code)        # 201 means "Created"
    print("JSON response:")
    print(json.dumps(response.json(), indent=2))
    # JSONPlaceholder only simulates the write: it returns the data with a new id
    # (101) but does not actually store it.


if __name__ == "__main__":
    main()
