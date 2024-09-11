import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel文件
data = pd.read_excel("总人口及分布.xls")
df = pd.DataFrame(data)

# 计算男女比例
df['男女性别比'] = df['男性'] / df['女性']

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(df['年份'], df['男女性别比'], marker='o', linestyle='-')
plt.title("1949-1982年中国男女性别比")
plt.xlabel("年份")
plt.ylabel("男女性别比")
plt.grid(True)
plt.show()
