# 导入Python内置的random模块，用于生成随机数/随机选择
import random

# 提示用户输入想要生成的密码长度，并将输入的字符串转换为整数类型
passlen = int(input("请输入密码长度："))

# 定义密码的字符集：包含小写字母、数字、大写字母
# 可以根据需要扩展，比如添加特殊符号 !@#$%^&*() 等
s = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 核心逻辑：生成随机密码
# random.sample(s, passlen)：从字符集s中随机选择passlen个不重复的字符，返回列表
# "".join(...)：将列表中的字符拼接成一个完整的字符串（密码）
p = "".join(random.sample(s, passlen))

# 输出最终生成的随机密码
print(p)
