import requests

URL = "https://v2.jokeapi.dev/joke/Any"

def get_joke():
    # sending get request and saving the response as response object
    try:
        r = requests.get(url = URL)
        data = r.json()
        return data
    except Exception as e:
        print(e.message, e.args)
    # extracting data in json format


# a = get_joke()
# ##print(a)

