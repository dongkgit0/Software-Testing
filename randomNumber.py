import random

passlen = int(input("请输入密码长度："))
s = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = "".join(random.sample(s, passlen))
print(p)