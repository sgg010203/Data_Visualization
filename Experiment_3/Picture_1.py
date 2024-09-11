import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['金融', '医疗保健', '市场业', '零售业', '制造业', '司法', '工程与科学', '保险业', '其他']
sizes = [172, 136, 135, 101, 80, 68, 50, 29, 41]

# 饼图
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('2009年5月饼状图')
plt.show()

# 环形图
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
plt.axis('equal')
plt.title('2009年5月环形图')
plt.show()
