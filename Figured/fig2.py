# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('BIC_pnum.csv')

del df['a']

plt.figure() 
df.plot(colormap='Dark2')
plt.show()

