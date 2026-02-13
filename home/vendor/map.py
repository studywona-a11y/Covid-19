# coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

def china_map(data_pair):
    Map(init_opts=opts.InitOpts(theme='dark', width='1600px', height='900px')
        ).add(
        series_name="",
        data_pair=data_pair,
        maptype="china",
        label_opts=opts.LabelOpts(
            is_show=True,
            position='inside',
        ),
        is_map_symbol_show=False,
    ).set_global_opts(
        title_opts=opts.TitleOpts(
            title="全国新冠疫情地图",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=24,
                font_family="Microsoft YaHei"),
            subtitle='统计时间截止至2020.09.21 21时',
            subtitle_textstyle_opts=opts.TextStyleOpts(
                font_size=12, font_family="Microsoft YaHei"),
        ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            formatter="{b} : 确诊{c}人",
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            dimension=0,
            pos_left="10",
            pos_bottom="20",
            pieces=[
                {'max': 9, 'min': 0, 'label': '0-9', 'color': '#FFFFCC'},
                {'max': 99, 'min': 10, 'label': '10-99', 'color': '#FFC4B3'},
                {'max': 499, 'min': 100, 'label': '100-499', 'color': '#FF9985'},
                {'max': 999, 'min': 500, 'label': '500-999', 'color': '#F57567'},
                {'max': 4999, 'min': 1000, 'label': '1000-4999', 'color': '#E64546'},
                {'max': 9999, 'min': 5000, 'label': '5000-9999', 'color': '#B80909'},
                {'max': 49999, 'min': 10000, 'label': '10000-49999', 'color': '#8A0808'},
                {'max': 99999, 'min': 50000, 'label': '>=50000', 'color': '#660000'}
            ]
        )
    ).render('中国疫情地图.html')


if __name__ == '__main__':
    df = pd.read_csv('china_province_data.csv')  # 利用pandas读取数据
    province_list = df[df['date']=='2020-09-21']['province'].tolist()  # 各省/区的名字列表
    data_list = df[df['date']=='2020-09-21']['confirmed'].tolist() # 数据
    data_pair = [x for x in zip(province_list, data_list)]
    china_map(data_pair)
