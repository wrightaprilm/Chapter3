# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('set_size.csv')
plt.figure() 
df['B'].hist().set_xlim(0,500)
plt.show()

