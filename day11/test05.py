def main():
    try:
        with open("image.png", "rb") as f:
            data = f.read()

        with open("image1.png", 'wb') as f2:
            f2.write(data)
    except IOError as ex:
        print(ex)
    finally:
        f.close()
        f2.close()


if __name__ == '__main__':
    main()
