import requests

url = "https://app.launchdarkly.com/api/v2/projects"

payload = {
  "key": "000011112",
  "name": "candysai"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "LD_PASS"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
#test
