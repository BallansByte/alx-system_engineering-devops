#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0. 
    Args:
        subreddit (str): The name of the subreddit
    Returns:
        int: Number of subscribers or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User-Agent"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
