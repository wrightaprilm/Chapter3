import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


aic = pd.read_csv("AIC_RF.csv" )
bic = pd.read_csv("BIC_RF.csv" )
aicc = pd.read_csv("AICC_RF.csv" )
merged_inner = pd.merge(left=aic, right=bic, left_on='Data Set', right_on='0')
merged_inner = pd.merge(left=merged_inner, right=aicc, left_on='Data Set', right_on='Data Set')
sizes = pd.read_csv('set_size.csv')
merged_inner = pd.merge(left=merged_inner, right=sizes, left_on='Data Set', right_on='1')

aic_scaled = merged_inner['Unnamed: 4_x'] / merged_inner['tax']
bic_scaled = merged_inner['3_y'] / merged_inner['tax']
aicc_scaled = merged_inner['Unnamed: 4_y'] / merged_inner['tax']
big_list = zip(aic_scaled, aicc_scaled, bic_scaled )
big_df = pd.DataFrame(big_list)
filtered = big_df[big_df < 1]

plt.figure()
filtered.plot(kind='hist', alpha=0.5)
plt.show()
