"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ""
    last_index = len(all_chars) - 1
    for _ in range(0, code_len):
        rand = random.randint(0, last_index)
        code += all_chars[rand]
    return code


def main():
    code = generate_code();
    print("code = %s" % code)


if __name__ == "__main__":
    main()
