# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('fig3_startingtree.csv')
plt.figure()
df['scaled'].plot(kind='hist')
plt.show()
