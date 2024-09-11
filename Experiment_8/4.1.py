import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_excel("出生率与死亡率.xls")

# 提取数据
years = data['年份']
birth_rate = data['出生率']
death_rate = data['死亡率']
natural_growth_rate = data['自然增长率']

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(years, birth_rate, label='出生率')
plt.scatter(years, death_rate, label='死亡率')
plt.scatter(years, natural_growth_rate, label='自然增长率')
plt.title('人口出生率、死亡率和自然增长率变化')
plt.xlabel('年份')
plt.ylabel('‰')
plt.legend()
plt.grid(True)
plt.show()
