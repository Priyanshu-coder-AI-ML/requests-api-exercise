"""Offline tests: the network is mocked, so they run anywhere (including CI)."""

import json
from unittest.mock import MagicMock, patch
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
import task1_get_posts
import task2_restaurant_json
import task3_post_request
import task4_query_params
import task5_custom_headers


def fake_response(json_data, status_code=200):
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


def test_task1_returns_first_five_titles():
    posts = [{"id": i, "title": f"title {i}"} for i in range(1, 101)]
    with patch("task1_get_posts.requests.get", return_value=fake_response(posts)) as mock_get:
        titles = task1_get_posts.get_first_titles(5)
    assert titles == ["title 1", "title 2", "title 3", "title 4", "title 5"]
    mock_get.assert_called_once_with(task1_get_posts.API_URL, timeout=10)


def test_task2_json_round_trip():
    json_string = task2_restaurant_json.to_json(task2_restaurant_json.restaurant)
    assert isinstance(json_string, str)
    assert json.loads(json_string) == task2_restaurant_json.restaurant
    for field in ("name", "location", "cuisines", "ratings"):
        assert field in json_string


def test_task3_posts_json_payload():
    reply = {**task3_post_request.new_playlist, "id": 101}
    with patch("task3_post_request.requests.post",
               return_value=fake_response(reply, 201)) as mock_post:
        response = task3_post_request.create_playlist(task3_post_request.new_playlist)
    assert response.status_code == 201
    assert response.json()["id"] == 101
    _, kwargs = mock_post.call_args
    assert kwargs["json"] == task3_post_request.new_playlist


def test_task4_sends_user_id_param_and_returns_ids():
    posts = [{"id": i, "userId": 2} for i in range(11, 21)]
    with patch("task4_query_params.requests.get", return_value=fake_response(posts)) as mock_get:
        ids = task4_query_params.get_post_ids_by_user(2)
    assert ids == list(range(11, 21))
    _, kwargs = mock_get.call_args
    assert kwargs["params"] == {"userId": 2}


def test_task5_sends_authorization_header():
    reply = {"headers": {"X-Custom-Header": "hello-from-python"}}
    with patch("task5_custom_headers.requests.get", return_value=fake_response(reply)) as mock_get:
        response = task5_custom_headers.fetch_with_headers("abc123")
    assert response.status_code == 200
    _, kwargs = mock_get.call_args
    assert kwargs["headers"]["Authorization"] == "Bearer abc123"
