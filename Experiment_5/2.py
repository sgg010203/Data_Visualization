from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

from pyecharts import options as opts
from pyecharts.charts import Sunburst


def sunburst() -> Sunburst:
    data = [
        opts.SunburstItem(
            name="古寨",
            children=[
                opts.SunburstItem(
                    name="山水",
                    value=15,
                    children=[
                        opts.SunburstItem(name="山峦叠翠", value=2),
                        opts.SunburstItem(
                            name="日落夕阳",
                            value=5,
                            children=[opts.SunburstItem(name="万家灯火", value=2)],
                        ),
                        opts.SunburstItem(name="水如明镜", value=4),
                    ],
                ),
                opts.SunburstItem(
                    name="建筑",
                    value=10,
                    children=[
                        opts.SunburstItem(name="博物馆", value=5,
                                          children=[opts.SunburstItem(name="宗教文化", value=1),
                                                    opts.SunburstItem(name="节日文化", value=2), ], ),
                        opts.SunburstItem(name="吊脚楼", value=3),
                    ],
                ),
            ],
        ),
        opts.SunburstItem(
            name="苗族",
            children=[
                opts.SunburstItem(
                    name="苗族人",
                    children=[
                        opts.SunburstItem(name="热情好客", value=1),
                        opts.SunburstItem(name="民风民俗", value=2),
                    ],
                )
            ],
        ),
    ]

    c = (
        Sunburst()
        .add(series_name="", data_pair=data, radius=[0, "90%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="贵州苗族古寨"),
                         toolbox_opts=opts.ToolboxOpts())
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


# 第一次渲染时候调用load_javasrcript文件
sunburst().load_javascript()
# 展示数据可视化图表
sunburst().render('文档霰.html')
