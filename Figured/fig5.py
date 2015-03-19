# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('tl_AIC_bayes.csv')
bic = pd.read_csv('tl_BIC_bayes.csv')
aicc = pd.read_csv('tl_AICC_bayes.csv')

aic.columns = ['set','aic']
bic.columns = ['set','bic']
aicc.columns = ['set','aicc']

merged_inner = pd.merge(left=aicc, right=bic, left_on='set', right_on='set')
mi = pd.merge(left=merged_inner, right=aic, left_on='set', right_on='set')
mi = mi.drop('set', axis=1)
mi = mi[mi > -5]
mi = mi[5 > mi]
plt.figure()
ax_list = mi.hist(sharex=True, sharey=True, bins=20)

ax_list[0][0].set_xlim((-1.5,1.5))
ax_list[0][0].set_ylim((0,300))
ax_list[0][1].set_xlim((-1.5,1.5))
ax_list[0][1].set_ylim((0,300))
plt.show()
