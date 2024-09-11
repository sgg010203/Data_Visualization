import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
beijing_data = pd.read_csv("beijing_AQI_2018.csv")
shanghai_data = pd.read_csv("shanghai_AQI_2018.csv")
guangzhou_data = pd.read_csv("guangzhou_AQI_2018.csv")
shenzhen_data = pd.read_csv("shenzhen_AQI_2018.csv")

# 将日期列转换为datetime类型
beijing_data['Date'] = pd.to_datetime(beijing_data['Date'])
shanghai_data['Date'] = pd.to_datetime(shanghai_data['Date'])
guangzhou_data['Date'] = pd.to_datetime(guangzhou_data['Date'])
shenzhen_data['Date'] = pd.to_datetime(shenzhen_data['Date'])

# 设置日期列为索引
beijing_data.set_index('Date', inplace=True)
shanghai_data.set_index('Date', inplace=True)
guangzhou_data.set_index('Date', inplace=True)
shenzhen_data.set_index('Date', inplace=True)

# 绘制北上广深每日AQI全年走势图
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(beijing_data['AQI'], label='北京', color='blue')
plt.plot(shanghai_data['AQI'], label='上海', color='green')
plt.plot(guangzhou_data['AQI'], label='广州', color='red')
plt.plot(shenzhen_data['AQI'], label='深圳', color='orange')
plt.title('2018年北上广深每日AQI全年走势图')
plt.xlabel('日期')
plt.ylabel('AQI指数')
plt.legend()
plt.grid(True)

# 绘制北上广深每日PM全年走势图
plt.subplot(1, 2, 2)
plt.plot(beijing_data['PM'], label='北京', color='blue')
plt.plot(shanghai_data['PM'], label='上海', color='green')
plt.plot(guangzhou_data['PM'], label='广州', color='red')
plt.plot(shenzhen_data['PM'], label='深圳', color='orange')
plt.title('2018年北上广深每日PM全年走势图')
plt.xlabel('日期')
plt.ylabel('PM值')
plt.legend()
plt.grid(True)
plt.show()

# 计算北上广深每个城市空气质量等级的数量
beijing_quality_counts = beijing_data['Quality_grade'].value_counts()
shanghai_quality_counts = shanghai_data['Quality_grade'].value_counts()
guangzhou_quality_counts = guangzhou_data['Quality_grade'].value_counts()
shenzhen_quality_counts = shenzhen_data['Quality_grade'].value_counts()

# 绘制北上广深全年空气质量情况的饼图
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.pie(beijing_quality_counts, labels=beijing_quality_counts.index, autopct='%1.1f%%')
plt.title('2018年 北京 空气质量情况')

plt.subplot(2, 2, 2)
plt.pie(shanghai_quality_counts, labels=shanghai_quality_counts.index, autopct='%1.1f%%')
plt.title('2018年 上海 空气质量情况')

plt.subplot(2, 2, 3)
plt.pie(guangzhou_quality_counts, labels=guangzhou_quality_counts.index, autopct='%1.1f%%')
plt.title('2018年 广州 空气质量情况')

plt.subplot(2, 2, 4)
plt.pie(shenzhen_quality_counts, labels=shenzhen_quality_counts.index, autopct='%1.1f%%')
plt.title('2018年 深圳 空气质量情况')
plt.show()
