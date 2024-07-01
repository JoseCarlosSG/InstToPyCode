import requests

url = "https://api.github.com/repos/CarlosPregunton/gitNotes"
token = "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"
headers = {
    "Authorization": f"token {token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Usuario autenticado: {data['full_name']}")
else:
    print(f"Error: {response.status_code}")


