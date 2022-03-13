import pandas as pd
import matplotlib.pyplot
from pylab import *

df_1 = pd.read_csv('Ze_1.csv')
df_2 = pd.read_csv('Ze_2.csv')
df_3 = pd.read_csv('Ze_3.csv')


def graph(df):
    x = df["Time(s)"]
    y = df["Ch 1  (V)"]
    z = df["Ch 2  (V)"]
    plot(x,y)
    plt.show()
graph(df_1)


'''
For LZ lab we need to


'''
