import requests
import os

url = "http://127.0.0.1:8000"


def test_users():
    urlTest = os.path.join(url, "users", "all")

    response = requests.post(url=urlTest)

    data = response.json()
    print(data)


if __name__ == "__main__":
    test_users()
