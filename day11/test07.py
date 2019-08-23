import requests
import json


def main():
    resp = requests.get("https://app1.coinegg.im/app/support/coininfolist")
    print(resp)
    data = json.loads(resp)
    print(data)


if __name__ == '__main__':
    main()
