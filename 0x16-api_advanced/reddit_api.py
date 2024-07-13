#!/usr/bin/python3
"""
reddit_api module
"""

import requests

def get_reddit_data(subreddit):
    """
    Fetches data from a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    headers = {'User-agent': 'your bot 0.1'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    subreddit = 'python'
    data = get_reddit_data(subreddit)
    if data:
        print(data)
    else:
        print("Failed to retrieve data")
