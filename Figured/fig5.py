# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('tl_aic_rax.csv')
bic = pd.read_csv('tl_BIC_rax.csv')
aicc = pd.read_csv('tl_AICC_rax.csv')

aic.columns = ['set','diff']
bic.columns = ['set','diff']
aicc.columns = ['set','diff']

merged_inner = pd.merge(left=aicc, right=bic, left_on='set', right_on='set')
mi = pd.merge(left=merged_inner, right=aic, left_on='set', right_on='set')

mi = aicc[aicc > -5]
mi = mi.drop('set',axis=1)
aicc.plot(kind='hist', bins=20, stacked=True, colormap='Dark2')
plt.show()
