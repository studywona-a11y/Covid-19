import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# 数据导入
df = pd.read_csv('../sym/sym.csv')
# 看一下数据是
df.head()
# 有无缺失值
df.isna().values.any()
# False 没有缺失值
# 获取特征值
X= df.iloc[:, :-1].values
# 获取标签值
Y = df.iloc[:,[-1]].values
# 使用sklearn 的DecisionTreeClassifier判断变量重要性
# 建立分类决策树模型对象
dt_model = DecisionTreeClassifier(random_state=1)
# 将数据集的维度和目标变量输入模型
dt_model.fit(X, Y)
# 获取所有变量的重要性
feature_importance = dt_model.feature_importances_
print(feature_importance)
# 结果如下
# array([0.20462132, 0.06426227, 0.16799114, 0.15372793, 0.07410088, 0.02786222, 0.09301948, 0.16519298, 0.04922178])
# 做可视化
X=range(len(df.columns[:-1]))
plt.bar(x=X, height=feature_importance)
plt.xticks(X, df.columns[:-1])
plt.show()