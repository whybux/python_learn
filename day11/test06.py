import json


def main():
    data = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }
    try:
        with open("test.json", "w") as f:
            json.dump(data, f)
    except IOError as ex:
        print(ex)
    finally:
        f.close()

    try:
        with open("test.json", "r") as f2:
            data2 = json.load(f2)
            print(data2)
    except Exception as ex:
        print(ex)
    finally:
        f2.close()

    data_st = json.dumps(data)
    print("data_str", data_st)

    data3 = json.loads(data_st)
    print("data3", data3)


if __name__ == '__main__':
    main()
