"""
用户身份验证

"""

userName = input("请输入用户名：")
password = input("请输入密码：")


if userName == "abc" and password == "123456":
    print("登录成功")
else:
    print("登录失败")