import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_csv("beijing_AQI_2018.csv")

# 将日期列转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 提取季度信息
data['Quarter'] = data['Date'].dt.quarter

# 提取AQI和PM数据
aqi_data = data[['Quarter', 'AQI']]
pm_data = data[['Quarter', 'PM']]

# 按季度分组并计算每个季度的数据
grouped_aqi = aqi_data.groupby('Quarter')['AQI'].apply(list)
grouped_pm = pm_data.groupby('Quarter')['PM'].apply(list)
print(grouped_aqi)


# 创建一个大的subplot网格
plt.figure(figsize=(16, 6))

# 绘制季度AQI箱型图
plt.subplot(1, 2, 1)
plt.boxplot(grouped_aqi.values, labels=['Q1', 'Q2', 'Q3', 'Q4'])
plt.title('北京每季度 AQI指数 (2018)')
plt.xlabel('季度')
plt.ylabel('AQI指数')
plt.grid(True)

# 绘制季度PM箱型图
plt.subplot(1, 2, 2)
plt.boxplot(grouped_pm.values, labels=['Q1', 'Q2', 'Q3', 'Q4'])
plt.title('北京每季度 PM值 (2018)')
plt.xlabel('季度')
plt.ylabel('PM值')
plt.grid(True)

# 调整布局，避免重叠
plt.tight_layout()

# 显示图
plt.show()

