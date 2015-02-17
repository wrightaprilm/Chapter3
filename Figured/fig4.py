# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

aic = pd.read_csv('AIC_final_like.csv')
aicc = pd.read_csv('AICC_final_like.csv')
bic = pd.read_csv('BIC_final_like.csv')
unpart = pd.read_csv('unpart_final_like.csv')
aic.columns = ['a','AIC']
aicc.columns = ['a','AICC']
bic.columns = ['a','BIC']
unpart.columns = ['a','Unpart']
merged_inner = pd.merge(left=aicc, right=bic, left_on='a', right_on='a')
merged_inner = pd.merge(left=merged_inner, right=aic, left_on='a', right_on='a')
mi = pd.merge(left=merged_inner, right=unpart, left_on='a', right_on='a')
aic_rel = mi['AIC'] - mi['Unpart']  
aicc_rel = mi['AICC'] - mi['Unpart']
bic_rel = mi['BIC'] - mi['Unpart']

df = pd.DataFrame(zip(aicc_rel, bic_rel, aic_rel))


filtered.plot(kind='hist', bins=20, stacked=True, colormap='Dark2')
plt.show()
