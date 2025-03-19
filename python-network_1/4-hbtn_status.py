#!/usr/bin/python3
"""
This script fetches the status of the specified URL using the `requests` package.
It sends a GET request to the URL 'https://alu-intranet.hbtn.io/status' and prints
the response body in a specific format as outlined in the prompt.

Usage:
    $ ./4-hbtn_status.py
    The script will print:
        Body response:
            - type: <class 'str'>
            - content: <response_body>

Module Requirements:
    - requests (installed via `pip install requests`)
"""

import requests

if __name__ == "__main__":
    # Send GET request to the URL
    response = requests.get('https://alu-intranet.hbtn.io/status')
    
    # Print the response body details in the specified format
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
