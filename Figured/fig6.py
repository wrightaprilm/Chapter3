# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('aic_bs.csv')
aic.columns = ['index','part']

aicc = pd.read_csv('AICC_bs.csv')
aicc.columns = ['index','part']

bic = pd.read_csv('BIC_bs.csv')
bic.columns = ['index','part']

merged_inner = pd.merge(left=aic, right=aicc, left_on='index', right_on='index')
merged_inner = pd.merge(left=merged_inner, right=bic, left_on='index', right_on='index')
mi = merged_inner.drop('index',axis = 1)
mi.plot(kind='hist', bins=20, stacked=True, colormap='Dark2')
plt.show()
