#-*- coding: utf-8 -*-
#主成分分析 降维
import pandas as pd

#参数初始化
inputfile = '1.xlsx'

data = pd.read_excel(inputfile, header = None) #读入数据

from sklearn.decomposition import PCA

# pca = PCA(n_components=0.9)   #保留所有成分
# pca.fit(data)
# # print(pca.components_) #返回模型的各个特征向量
# print(pca.explained_variance_ratio_ )#返回各个成分各自的方差百分比(也称贡献率）

pca = PCA(n_components=0.9)
pca.fit(data)
low_d = pca.transform(data)  # 用它来降低维度
pd.DataFrame(low_d).to_excel('output.xlsx')  #