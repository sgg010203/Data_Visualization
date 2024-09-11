import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_excel("年龄结构与抚养比.xls")

# 提取数据
years = data['年份']
age_0_14 = data['0-14岁']
age_15_64 = data['15-64岁']
age_65_above = data['65岁及以上']

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(years, age_0_14, label='0-14岁')
plt.scatter(years, age_15_64, label='15-64岁')
plt.scatter(years, age_65_above, label='65岁及以上')
plt.title('年龄结构变化')
plt.xlabel('年份')
plt.ylabel('人口数')
plt.legend()
plt.grid(True)
plt.show()
