def main():
    try:
        with open("abc.text", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("文件未找到")
    except LookupError:
        print("指定未知的编码")
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()
