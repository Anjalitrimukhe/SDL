
import pandas as pd

ds=pd.read_csv('Game_medal.csv',encoding='ISO-8859-1')

ds.head()
ds.tail()
ds.shape
ds.shift
ds.describe()
ds.info()
ds.plot()
 import matplotlib.pyplot as p
 
 p.xlabel('records')
 p.ylabel('year of event')
 p.title('game_graph')
 p.plot(ds.edition,label='year of event',color='green',linewidth=3)
 fig=p.gcf()
 ds.plot()
 fid.savefig('figu.png')
