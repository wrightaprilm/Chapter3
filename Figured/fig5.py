# coding: utf-8
aic = pd.read_csv('AIC_diffed.csv')
bic = pd.read_csv('BIC_diffed.csv')
aicc = pd.read_csv('AICC_diffed.csv')

aic.columns = ['set','diff']
bic.columns = ['set','diff']
aicc.columns = ['set','diff']

merged_inner = pd.merge(left=aicc, right=aic, left_on='set', right_on='set')
merged_inner = pd.merge(left=merged_inner, right=bic, left_on='set', right_on='set')

mi = mi[mi > -5]
mi.plot(kind='hist', alpha = .5, bins=20)
plt.show()
