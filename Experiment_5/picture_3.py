from pyecharts import options as opts
from pyecharts.charts import ThemeRiver
import pandas as pd

# 从 Excel 文件中读取数据
file_path = "complaints.xls"
data = pd.read_excel(file_path)

# 处理数据，提取所需列
v1 = data[['date', 'count', 'category']].values.tolist()


# 绘制主题河流图
def themeriver() -> ThemeRiver:
    c = (
        ThemeRiver()
        .add(
            ["产品质量", "服务态度", "售后服务"],
            v1,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年8月份客户投诉分析",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True, item_width=40, item_height=20,
                                        textstyle_opts=opts.TextStyleOpts(font_size=16)))
        # .set_series_opts(label_opts=opts.LabelOpts(font_size = 16))
        .set_series_opts(label_opts=True)
    )
    return c


# 第一次渲染时候调用load_javasrcript文件
themeriver().load_javascript()
# 展示数据可视化图表
themeriver().render('河流图.html')
