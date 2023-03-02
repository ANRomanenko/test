import requests
from apikey import API_TOKEN



# params = {"q": "Kiev", "appid": API_TOKEN, "units": "metric"}
#
# url = "https://api.openweathermap.org/data/2.5/weather"
#
# r = requests.get(url, params=params)

# params = {"q": "Kiev", "appid": API_TOKEN, "units": "metric"}
data = {"custname": "name", "custtel": "pass", "custemail": "", "delivery": "", "comments": "",}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-63ff2468-4d9902007c37936579de0e12"
  }

url = "https://httpbin.org/post"
url_1 = "https://httpbin.org/forms/post"

variable = requests.Session()

test = variable.get(url_1)
r = variable.post(url, headers=headers, data=data)



# print(r.status_code)
# print(r.headers)
print(r.text)
# print(r.json())
# print(r.json())
# print(r)

# x = r.json()
# print(x["weather"][0]["main"])