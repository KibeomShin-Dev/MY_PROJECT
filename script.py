import requests

r = requests.get("naver.com")
print(r.status_code)
