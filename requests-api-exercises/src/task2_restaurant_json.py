"""Task 2: Build a Zomato-style restaurant dictionary and convert it to JSON."""

import json

restaurant = {
    "name": "Spice Garden",
    "location": {
        "address": "12 MG Road",
        "city": "Vadodara",
        "state": "Gujarat",
        "pincode": "390001",
    },
    "cuisines": ["North Indian", "Chinese", "Mughlai"],
    "ratings": {
        "average": 4.3,
        "total_reviews": 1287,
        "food": 4.5,
        "service": 4.1,
        "ambience": 4.2,
    },
    "price_for_two": 600,
    "is_open": True,
    "delivery": True,
    "offers": None,
}


def to_json(data):
    """Convert a Python dictionary into a formatted JSON string."""
    return json.dumps(data, indent=2, ensure_ascii=False)


def main():
    json_string = to_json(restaurant)
    print(json_string)

    # Optional: prove the conversion is lossless by converting it back.
    assert json.loads(json_string) == restaurant
    print("\nRound trip check passed: JSON string converts back to the same dictionary.")


if __name__ == "__main__":
    main()
