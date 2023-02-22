# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 01:58:03 2023

@author: ZJZ
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style='white')  #设置风格

df = pd.read_excel("./AHP和熵权TOPSIS结果的灰色预测绘图.xlsx")
#df = pd.read_excel("./模型拟合结果表1.xlsx")

plt.figure(dpi=600)
li = sns.color_palette()
#sns.palplot(li)
color = [li[2],li[3]]

g = sns.lineplot(data=df, x='Year',y='value',hue='Kind',style='Kind',markers=True,palette=color)
#sns.despine(top=True,right=True)

g.set(xlabel="Year", ylabel="Value")

plt.savefig("./AHP+SQF.pdf")
#plt.savefig("./SQF.pdf")
