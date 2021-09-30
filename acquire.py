import pandas as pd
import requests

def gather_info(url):
    response = requests.get(url)
    print(response.ok)
    print(response.status_code)
    print(response.text)
    return data = response.json()

**********