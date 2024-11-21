import requests

url = "https://app.launchdarkly.com/api/v2/projects"

payload = {
  "key": "69",
  "name": "Rockey"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "api-205f67ed-bc69-45c2-b984-4e179818b659"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
#test
