import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_csv("beijing_AQI_2018.csv")

# 设置字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置字体为宋体

# 计算每个空气质量等级的数量
quality_counts = data['Quality_grade'].value_counts()
print(type(quality_counts))
# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(quality_counts, labels=quality_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('北京空气质量分布 (2018)')
plt.axis('equal')  # 使饼图比例相等
plt.show()
