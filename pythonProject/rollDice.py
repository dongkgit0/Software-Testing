# 导入Python内置的random模块，用于生成随机整数
import random

# 定义一个模拟掷骰子的函数
def roll_dice():
    # random.randint(1, 6)：生成1到6之间（包含1和6）的随机整数，模拟骰子的点数
    return random.randint(1, 6)

# 调用掷骰子函数，并使用f-string格式化输出结果，展示掷出的点数
print(f"你掷出了一个 {roll_dice()}")
