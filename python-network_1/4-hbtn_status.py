#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests

if __name__ == "__main__":
    # Update the URL to the correct server
    url = 'http://0.0.0.0:5050/status'

    # Add headers to mimic a browser request (optional but useful for some websites)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Fetch the URL
    r = requests.get(url, headers=headers)
    
    # Get the text of the response
    t = r.text.strip()  # Strip whitespace around the content

    # Print the output in the expected format
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
