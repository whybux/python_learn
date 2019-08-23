import math


def is_prime(num):
    is_p = True
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            is_p = False
            break
    return is_p


def main():
    files = ["a.txt", "b.txt", "c.txt"]
    fs = []
    try:
        for file in files:
            fs.append(open(file, "w", encoding="UTF-8"))

        for num in range(1, 10000):
            if is_prime(num):
                if num < 100:
                    fs[0].write(str(num) + "\n")
                elif num < 1000:
                    fs[1].write(str(num) + "\n")
                else:
                    fs[2].write(str(num) + "\n")
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for f in fs:
            f.close()


if __name__ == '__main__':
    main()
