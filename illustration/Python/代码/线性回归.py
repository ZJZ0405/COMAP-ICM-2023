# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:36:27 2023

@author: ZJZ
"""


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style='ticks')  #设置风格
plt.figure(dpi=600)
df = pd.read_excel("./US-GGDP-GGDP%.xlsx")

g = sns.regplot(data=df, x='GDP(Trillion dollars)', y='GGDP')
sns.despine()
g.set(xlabel="US-GDP(Trillion dollars)", ylabel="US-GGDP")


plt.savefig("./US-GGDP-GDP.pdf")
