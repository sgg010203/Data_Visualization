import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV数据
data = pd.read_csv('2020年前3个季度客户流失数据.csv')

# 设置雷达图的标签
labels = list(data.columns[1:])

# 设置雷达图的数据
stats = data.iloc[:, 1:].values

# 绘制雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
stats = np.concatenate((stats, stats[:,[0]]), axis=1)
angles += angles[:1]

for i in range(len(data)):
    ax.plot(angles, stats[i], linewidth=1, linestyle='solid')

# 添加每个数据点的标签
ax.set_thetagrids(np.degrees(angles[:-1]), labels)

# 设置雷达图的标题
plt.title('2020年前3个季度客户流失数据 雷达图')

# 显示雷达图
plt.show()