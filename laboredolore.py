import requests

def get_api_call_data(url):
    """Makes a GET request to the specified URL and returns the JSON response.

    Args:
        url: The URL to make the request to.

    Returns:
        The JSON response from the request.
    """

    response = requests.get(url)
    response.raise_for_status()
    return response.json()
