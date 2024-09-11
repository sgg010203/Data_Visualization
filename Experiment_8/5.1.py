import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_excel("出生率与死亡率.xls")

# 提取数据
birth_rate = data['出生率']
natural_growth_rate = data['自然增长率']

# 绘制线性回归图
plt.figure(figsize=(10, 6))
plt.scatter(birth_rate, natural_growth_rate, label='Data')
plt.title('人口出生率与自然增长率线性回归')
plt.xlabel('人口出生率')
plt.ylabel('自然增长率')
plt.grid(True)

# 添加线性回归线
z = np.polyfit(birth_rate, natural_growth_rate, 1)
p = np.poly1d(z)
plt.plot(birth_rate, p(birth_rate), "r--", label='Regression Line')
plt.legend()
plt.show()
