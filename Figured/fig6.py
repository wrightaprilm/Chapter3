# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('AIC_bs.csv')
aic.columns = ['index','set','part','unpart']
aic['diffAIC'] = aic['part'] - aic['unpart']

aicc = pd.read_csv('AICC_bs.csv')
aicc.columns = ['index','set','part','unpart']
aicc['diffAICC'] = aicc['part'] - aicc['unpart']

bic = pd.read_csv('BIC_bs.csv')
bic.columns = ['index','set','part','unpart']
bic['diffBIC'] = bic['part'] - bic['unpart']

aicc = aicc.drop(['part','index','unpart'], axis=1)
aic = aic.drop(['part','index','unpart'], axis=1)
bic = bic.drop(['part','index','unpart'], axis=1)

merged_inner = pd.merge(left=aic, right=aicc, left_on='set', right_on='set')
merged_inner = pd.merge(left=merged_inner, right=bic, left_on='set', right_on='set')
mi = merged_inner.drop('set',axis = 1)
mi.plot(kind = 'hist', alpha = .5)
plt.show()
