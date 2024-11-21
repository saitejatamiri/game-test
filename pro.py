import requests

url = "https://app.launchdarkly.com/api/v2/projects"

payload = {
  "key": "KEY",
  "name": "PRO"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "TOCK"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
