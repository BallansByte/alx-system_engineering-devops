#!/usr/bin/python3
import requests
"""
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    
    Args:
        subreddit (str): The name of the subreddit
    
    Returns:
        int: Number of subscribers or 0 if invalid subreddit
    """
def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"(link unavailable)"
    headers = {"User-Agent": "My Reddit API Client/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
