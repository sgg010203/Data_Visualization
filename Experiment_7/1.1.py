import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_csv("beijing_AQI_2018.csv")

# 将日期列转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])

# 设置日期列为索引
data.set_index('Date', inplace=True)

# 创建一个大的subplot网格
plt.figure(figsize=(16, 12))

# 每日AQI全年走势图
plt.subplot(2, 2, 1)
plt.plot(data['AQI'], color='blue')
plt.title('每日AQI全年走势图')
plt.xlabel('月份')
plt.ylabel('AQI指数')
plt.grid(True)

# 每日PM2.5全年走势图
plt.subplot(2, 2, 2)
plt.plot(data['PM'], color='green')
plt.title('每日PM2.5全年走势图')
plt.xlabel('月份')
plt.ylabel('PM指数')
plt.grid(True)

# 月均AQI全年走势图
monthly_aqi = data['AQI'].resample('M').mean()
plt.subplot(2, 2, 3)
plt.plot(monthly_aqi, color='red')
plt.title('月均AQI全年走势图')
plt.xlabel('月份')
plt.ylabel('AQI指数')
plt.grid(True)

# 月均PM2.5全年走势图
monthly_pm25 = data['PM'].resample('M').mean()
plt.subplot(2, 2, 4)
plt.plot(monthly_pm25, color='purple')
plt.title('月均PM2.5全年走势图')
plt.xlabel('月份')
plt.ylabel('PM指数')
plt.grid(True)

# 调整布局，避免重叠
plt.tight_layout()

# 显示图
plt.show()
