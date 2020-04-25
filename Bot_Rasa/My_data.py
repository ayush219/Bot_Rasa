import pandas as pd
import numpy as np

df= pd.read_csv('populationdata.csv')
city_name='kolkata'

d=df[df['city']==city_name]['population']
f=df[df.city==city_name]['population']
p=df.query('city == @city_name')['population']

e=d.values[0]
s=str(d)

index=np.where(df["city"] == city_name )
i=index[0][0]

s=df.at[i,'population']