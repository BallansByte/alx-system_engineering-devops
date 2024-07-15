#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0


if __name__ == '__main__':
    subreddit = 'guns'
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers}")
