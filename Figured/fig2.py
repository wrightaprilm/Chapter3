# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('./data/BIC_pnum.csv')

del df['a']

plt.figure()
ax_list = df.plot(kind='scatter', x ='a',y=['AIC','AICC','BIC'], sharex=True, sharey=True)
ax_list[0][0].set_xlim((0,1))

ax_list[0][1].set_xlim((0,1))
ax_list[0][1].set_ylim((0,300))
ax_list[0][2].set_xlim((0,1))
ax_list[0][2].set_ylim((0,300))
plt.show()

