import requests


def outer(url):
    # url = "https://www.baidu.com"
    def get():
        response = requests.get(url)
        print(len(response.text))

    return get


get = outer("https://www.baidu.com")
get()
