import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel文件
data = pd.read_excel("总人口及分布.xls")

# 提取年份和人口数据
years = data["年份"]
population = data["总人口"]

# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(years, population, marker='o', linestyle='-')
plt.title("2000-2019年中国人口总数分析")
plt.xlabel("年份")
plt.ylabel("人口总数")
plt.grid(True)
plt.show()
