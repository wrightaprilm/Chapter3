# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('rax_aic_bs.csv')
aic.columns = ['index','aic']

aicc = pd.read_csv('rax_aicc_bs.csv')
aicc.columns = ['index','aicc']

bic = pd.read_csv('rax_bic_bs.csv')
bic.columns = ['index','bic']

merged_inner = pd.merge(left=aicc, right=bic, left_index=True, right_index=True)
merged_inner = pd.merge(left=merged_inner, right=aic, left_index=True, right_index=True)
mi = merged_inner.drop(['index', 'index_x', 'index_y'],axis = 1)

plt.figure()
ax_list = mi.hist(sharex=True, sharey=True)
ax_list[0][0].set_xlim((-100,100))
ax_list[0][0].set_ylim((0,2500))
plt.show()

