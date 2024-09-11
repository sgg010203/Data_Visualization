import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data = {
    'A': [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9],
    'B': [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1],
    'C': [3, 8, 3, 3, 5, 3, 3, 5, 4, 12],
    'D': [23, 18],
    'E': [1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1],
    'F': [31],
    'G': [5, 9.3, 8.1, 12, 4, 3, 2],
    'H': [12, 3, 3]
}

fig, ax = plt.subplots()

# 绘制模块层级图
for i, (module, values) in enumerate(data.items()):
    ax.plot([i+1]*len(values), values, marker='o', linestyle='', label=module)

ax.set_xlabel('类别')
ax.set_ylabel('值')
ax.set_title('模块层级图')
ax.legend()

plt.show()
