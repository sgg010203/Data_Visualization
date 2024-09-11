import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
categories = ['种族问题', '教育', '恐怖活动', '能源政策', '外交事务', '环境', '宗教政策', '税收', '医疗保健政策',
              '经济', '就业政策', '贸易政策', '外来移民']
support = [52, 49, 48, 47, 44, 43, 41, 41, 40, 38, 36, 31, 29]
oppose = [38, 40, 45, 42, 48, 51, 53, 54, 57, 59, 57, 64, 62]
no_opinion = [10, 11, 7, 11, 8, 6, 6, 5, 3, 3, 7, 5, 9]

# 绘图
fig, ax = plt.subplots()
bar_width = 0.4
index = range(len(categories))

bar1 = ax.bar(index, support, bar_width, color='blue', label='支持')
bar2 = ax.bar(index, oppose, bar_width, color='green', label='反对', bottom=support)
bar3 = ax.bar(index, no_opinion, bar_width, color='red', label='不发表意见',
              bottom=[support[i] + oppose[i] for i in range(len(support))])

# 添加标签和数据
for i in range(len(categories)):
    ax.text(i, support[i] / 2, str(support[i]), ha='center', va='center', color='white')
    ax.text(i, support[i] + oppose[i] / 2, str(oppose[i]), ha='center', va='center', color='white')
    ax.text(i, support[i] + oppose[i] + no_opinion[i] / 2, str(no_opinion[i]), ha='center', va='center', color='white')

# 设置x轴标签
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45, ha='right')

# 设置图例
ax.legend()

plt.title('奥巴马总统支持率的民意调查')
plt.tight_layout()
plt.show()
