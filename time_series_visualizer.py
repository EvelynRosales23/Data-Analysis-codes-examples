import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates = True)

up = df['value'].quantile(0.975)
down = df['value'].quantile(0.025)
df = df[(df['value'] >= down) & (df['value'] <= up)]

def draw_line_plot():
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(df, 'b-')
    plt.show()

def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar.plot(kind="bar")
    plt.title("Months")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.show()

def draw_box_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    fig, axes = plt.subplots(1,2,figsize=(15, 5))
    sns.boxplot(data=df_bar, x=df_bar["year"], y=df_bar["value"], ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Years")
    axes[0].set_ylabel("Page Views")

    order = ["January", "February", "March", "April", "May", "June", "July", "August", "September"
             , "October", "November", "December"]
    sns.boxplot(data=df_bar, x=df_bar["month"], y=df_bar["value"], ax=axes[1], order=order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Months")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    plt.show()
#x = draw_line_plot()
#y = draw_bar_plot()
z = draw_box_plot()
print(z)