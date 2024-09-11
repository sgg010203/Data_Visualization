import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import xlrd


# 读取 Excel 文件
df = pd.read_excel('complaints.xls')

# 提取需要的数据列
data = df[['date', 'count', 'category']].values.tolist()
data['category'] = pd.to_numeric(data['category'])

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
# angles += angles[:1]

# 绘制旭日图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, data, color='blue', alpha=0.25)
ax.plot(angles, data, color='blue', linewidth=2)
plt.show()
