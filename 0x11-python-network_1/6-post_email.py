#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=payload)
    print(r.text)
