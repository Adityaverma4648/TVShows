import requests

url = "https://youtube-v31.p.rapidapi.com/search"

headers = {
    "X-RapidAPI-Key": "4fbcfea748msh22a8e752a443b6dp15a8afjsn3b3623db9eae",
    "X-RapidAPI-Host": "youtube-v31.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)