import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取 Excel 文件
data = pd.read_csv("2020年上半年各地区利润表.csv")

# 提取需要绘制的数据列
columns_to_plot = ["地区", "一月", "二月", "三月", "四月", "五月", "六月"]

# 绘制平行坐标系图
plt.figure(figsize=(10, 6))
pd.plotting.parallel_coordinates(data[columns_to_plot], "地区", colormap='viridis')
plt.title("2020年上半年各地区利润表 平行坐标系")
plt.xlabel("月份")
plt.ylabel("利润")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
