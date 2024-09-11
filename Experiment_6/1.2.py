import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel文件
data = pd.read_excel("经营数据.xls")

# 将不同类型的订单映射到RGB颜色
color_map = {'general': 'r', 'high': 'g', 'low': 'b'}
colors = data['type'].str.lower().map(color_map)

# 创建散点图矩阵
scatter_matrix = pd.plotting.scatter_matrix(data[['sales', 'profit', 'amount', 'discount']], c=colors, figsize=(10, 10),
                                            hist_kwds={'bins': 20}, grid=True)

# 添加标题
for ax in scatter_matrix.ravel():
    ax.set_xlabel(ax.get_xlabel(), fontsize=10)
    ax.set_ylabel(ax.get_ylabel(), fontsize=10)

plt.title('经营数据 散点图矩阵')
# 显示图表
plt.show()
