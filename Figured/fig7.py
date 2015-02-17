# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

sets = pd.read_csv('set_size.csv')
aic = pd.read_csv('AIC_final_like.csv')
aicRF = pd.read_csv('AIC_RF.csv')
aic.columns = ['set','L']
aic = pd.merge(left=aic, right=aicRF, left_on='set', right_on='Data Set')
aic = pd.merge(left=aic, right=sets, left_on='set', right_on='1')

aic = aic.drop(['1_x','3','set','char','1_y'], axis=1)
aic['scaled'] = aic['Unnamed: 4']/aic['tax']
aic = aic.drop(['Data Set', '2','tax','Unnamed: 4'], axis=1)

BIC = pd.read_csv('BIC_final_like.csv')
BICCRF = pd.read_csv('BIC_RF.csv')
BIC.columns = ['set','L']
BICRF = BICRF.drop(['1','2'],axis=1)
BIC = pd.merge(left=BIC, right=BICRF, left_on='set', right_on='Data Set')
BIC = pd.merge(left=BICC, right=BICCRF, left_on='set', right_on='0')

BIC = BIC.drop(['1_x','3','set','char','1_y'], axis=1)
BIC['scaled'] = BIC['Unnamed: 4']/aic['tax']
BIC = BIC.drop(['set','0','3','1','tax','char'], axis=1)


AICC = pd.read_csv('AICC_final_like.csv')
AICCRF = pd.read_csv('AICC_RF.csv')
AICC.columns = ['set','L']
AICCRF = AICCRF.drop(['1','2'],axis=1)
AICC = pd.merge(left=AICC, right=AICCRF, left_on='set', right_on='Data Set')
AICC = pd.merge(left=AICC, right=Data Set, left_on='sets', right_on='1')

AICC = AICC.drop(['1_x','3','set','char','1_y'], axis=1)
AICC['scaled'] = AICC['Unnamed: 4']/AICC['tax']
AICC = AICC.drop(['set','0','3','1','tax','char'], axis=1)


aicc = aicc[aicc['scaled'] < 1]
aic = aic[aic['scaled'] < 1]
bic = bic[bic['scaled'] < 1]

aicc = abs(aicc)
aic = abs(aic)
bic = abs(bic)

ax = aic.plot(kind='scatter', x='L', y='scaled',color='LightBlue', label='AIC')
ax1 = bic.plot(kind='scatter', x='L', y='scaled',color='purple', label='BIC')
aicc.plot(kind='scatter', x='L', y='scaled', color='salmon', label='AICC', ax=ax)
plt.show()

