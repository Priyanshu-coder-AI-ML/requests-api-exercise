"""Task 1: Send a GET request and print the titles of the first 5 posts."""

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def get_first_titles(count=5):
    """Return the titles of the first `count` posts."""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()          # raise an error for 4xx / 5xx responses
    posts = response.json()              # parse the JSON body into a list of dicts
    return [post["title"] for post in posts[:count]]


def main():
    try:
        titles = get_first_titles(5)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    print("Titles of the first 5 posts:")
    for number, title in enumerate(titles, start=1):
        print(f"{number}. {title}")


if __name__ == "__main__":
    main()
