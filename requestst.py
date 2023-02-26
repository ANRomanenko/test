import requests
from PIL import image

url = 'https://api.github.com/events'

# payload = {"key1": "value1", 'key2': ['value2', 'value3']}

r = requests.get(url)

r.encoding = "ISO-8859-1"

print(r.encoding)

# with open('comic.jpg', 'wb') as file:
#     file.write(res.content)


