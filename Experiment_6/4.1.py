import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 假设你已经完成了数据加载、标准化和PCA处理
data = np.loadtxt('经营数据.txt')

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# 可视化
plt.figure(figsize=(8, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.title('主成分分析 数据可视化')
plt.xlabel('主成分 1')
plt.ylabel('主成分 2')
plt.grid(True)
plt.show()