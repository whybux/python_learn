import time


def main():
    with open("abc.text", "r") as f:
        print(f.read())

    with open("abc.text", "r") as f:
        for line in f:
            print(line, end="")
            time.sleep(0.5)

    with open("abc.text", "r") as f:
        lines = f.readlines()

    print(lines)


if __name__ == '__main__':
    main()
