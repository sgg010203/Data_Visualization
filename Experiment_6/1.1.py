import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建数据
data = pd.read_csv('经营数据.csv')

df = pd.DataFrame(data)

# 绘制散点图矩阵
sns.pairplot(df, hue='type')
plt.title('经营数据 散点图矩阵')
plt.show()
