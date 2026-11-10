"""Task 4: Filter posts with a query parameter (userId=2) and print their IDs."""

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def get_post_ids_by_user(user_id):
    """Return the IDs of all posts written by `user_id`."""
    # requests builds the URL for us: .../posts?userId=2
    response = requests.get(API_URL, params={"userId": user_id}, timeout=10)
    response.raise_for_status()
    return [post["id"] for post in response.json()]


def main():
    try:
        post_ids = get_post_ids_by_user(2)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    print(f"Found {len(post_ids)} posts for userId=2")
    print("Post IDs:", post_ids)


if __name__ == "__main__":
    main()
