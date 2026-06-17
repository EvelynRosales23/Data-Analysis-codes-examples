import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Import the data from medical_examination.csv 
#and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")

#Add an overweight column to the data.
BMI = (df['weight']/(df['height']**2))*10000
overweight = (BMI > 25).astype(int)

df['overweight'] = overweight
#Normalize data by making 0 always good and 1 always bad. 
df['cholesterol'].loc[df['cholesterol']==1] = 0
df['cholesterol'].loc[df['cholesterol'] > 1] = 1
df['gluc'].loc[df['gluc'] == 1] = 0
df['gluc'].loc[df['gluc'] > 1] = 1

def draw_cat_plot():    
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    df_cat = df_cat.rename(columns={'total': 'total'})

    cat = sns.catplot(
        data= df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ) 
    fig = cat.figure
    
    plt.show()

def draw_heat_map():
    df_heat = df[
        (df['ap_hi'] >= df['ap_lo']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
        ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr)) #los 1 ocultan
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .5},
        ax=ax
    )
    plt.show()
    
#print(df.info())
x = draw_heat_map()
y = draw_cat_plot()
print(y)