import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


aic = pd.read_csv("aic.csv" )
bic = pd.read_csv("bic.csv" )
aicc = pd.read_csv("aicc.csv" )
sizes = pd.read_csv('set_size')
sizes.columns = ['set','tax','char']
merged_inner = pd.merge(left=aicc, right=bic, left_on='0', right_on='0')
merged_inner = pd.merge(left=merged_inner, right=aic, left_on='0', right_on='0')
merged_inner = pd.merge(left=merged_inner, right=sizes, left_on='0', right_on='set')

aicc_scaled = merged_inner['1_x'] / (2*(merged_inner['tax'] -3))
bic_scaled = merged_inner['1_y'] / (2*(merged_inner['tax'] -3))
aic_scaled = merged_inner['1'] / (2*(merged_inner['tax'] -3))
big_list = zip(aicc_scaled, bic_scaled, aic_scaled )
big_df = pd.DataFrame(big_list)
big_df.columns = ['aicc','bic','aic']
filtered = big_df[big_df < 1]

plt.figure()
ax_list = big_df.hist(sharex=True, sharey=True)
ax_list[0][0].set_xlim((0,1))
ax_list[0][0].set_ylim((0,300))
ax_list[0][1].set_xlim((0,1))
ax_list[0][1].set_ylim((0,300))
ax_list[0][2].set_xlim((0,1))
ax_list[0][2].set_ylim((0,300))
plt.show()
