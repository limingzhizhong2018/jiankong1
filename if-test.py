#1.提示并获取用户名
userName = input("请输入用户名：")

#2、提示并获取密码

passwd = input("请输入密码：")
#3、判断用户名和密码都相等，根据判断结果显示信息


if userName == "111" and passwd == "111":
    print("登陆成功")
else:
    i = 0
    while i < 3:
        print("用户名密码错误")
        userName = input("请输入用户名：")
        passwd = input("请输入密码：")
        if userName == "111" and passwd == "111":
            print("登陆成功")
            break
        i += 1
    else:
        print("用户锁定")
