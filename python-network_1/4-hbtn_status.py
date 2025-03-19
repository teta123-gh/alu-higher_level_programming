#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""


import requests


if __name__ == "__main__":
    response = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
