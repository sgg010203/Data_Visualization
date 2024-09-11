import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_csv("beijing_AQI_2018.csv")

# 将日期列转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 提取年份、月份和日期
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# 提取PM数据
pm_data = data[['Year', 'Month', 'Day', 'PM']]
print(pm_data)
# 创建日历热力图
plt.figure(figsize=(10, 8))
sns.heatmap(
    pm_data.pivot_table(index='Month', columns='Day', values='PM', aggfunc='mean'),
    cmap='YlGnBu',  # 设置热图的颜色映射，这里使用的是黄绿蓝色映射，表示从低值到高值的过渡色
    annot=True,  # 启用单元格注释，即在热图上显示每个单元格的数值
    fmt=".1f",  # 指定注释数值的格式，这里是浮点数，保留一位小数
    linewidths=0.5  # 设置单元格之间的分隔线宽度，这里设置为0.5个单位
)

plt.title('2018年北京PM2.5指数日历热力图')
plt.xlabel('日')
plt.ylabel('月')
plt.show()
