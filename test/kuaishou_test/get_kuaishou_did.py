"""
动态获取did
"""
import requests

url = "http://127.0.0.1:9001/rendered_by_playwright/requests"

payload = {
    "url": "https://www.kuaishou.com/new-reco",
    "return_type": "cookies",
    "browser_type": "firefox",
    "timeout": 15
}
headers = {"content-type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)