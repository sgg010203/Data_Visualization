import pandas as pd
import plotly.express as px

# 读取数据
data = pd.read_csv("2020年上半年各地区利润表.csv")

# 定义评估等级的数值映射字典
evaluation_mapping = {'差': 1, '一般': 2, '好': 3, '优秀': 4}

# 将评估列的字符串值转换为数值
data['评估'] = data['评估'].map(evaluation_mapping)

a = data.iloc[:, :-1]

# 绘制平行坐标系图
fig = px.parallel_coordinates(data, color='评估',
                              color_continuous_scale=px.colors.sequential.Viridis,
                              color_continuous_midpoint=2,
                              title='2020年上半年各地区利润 平行坐标系')

fig.show()
