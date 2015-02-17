import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


aic = pd.read_csv("AIC_RF_bayes.csv" )
bic = pd.read_csv("BIC_RF_bayes.csv" )
aicc = pd.read_csv("AICC_RF_bayes.csv" )
sizes = pd.read_csv('set_size')
sizes.columns = ['set','tax','char']
merged_inner = pd.merge(left=aicc, right=bic, left_on='0', right_on='0')
merged_inner = pd.merge(left=merged_inner, right=aic, left_on='0', right_on='0')
merged_inner = pd.merge(left=merged_inner, right=sizes, left_on='0', right_on='set')

aic_scaled = merged_inner['Unnamed: 4_x'] / merged_inner['tax']
bic_scaled = merged_inner['3_y'] / merged_inner['tax']
aicc_scaled = merged_inner['Unnamed: 4_y'] / merged_inner['tax']
big_list = zip(aicc_scaled, bic_scaled, aic_scaled )
big_df = pd.DataFrame(big_list)
big_df.columns = ['aicc','bic','aic']
filtered = big_df[big_df < 1]

plt.figure()
filtered.plot(kind='hist', bins=20, stacked=True, colormap='Dark2')

plt.show()
