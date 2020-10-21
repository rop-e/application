import requests
from urllib.parse import urlencode


def extract_lat_lng(address, data_type="json"):
    api_key = "AIzaSyBxXZJ9LqBs52KEe5mYTSR4n-JxjTZ8rjU"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    latlng = {}

    if r.status_code not in range(200, 299):
        return {}

    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except Exception:
        pass

    return latlng.get("lat"), latlng.get("lng")
