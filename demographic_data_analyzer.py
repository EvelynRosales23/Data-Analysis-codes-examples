import pandas as pd

df = pd.read_csv("adult.data.csv")
def calculate_demografic_data():
    white = (df['race'] == 'White').sum()
    black = (df['race'] == 'Black').sum()
    asian = (df['race'] == 'Asian-Pac-Islander').sum()
    amer = (df['race'] == 'Amer-Indian-Eskimo').sum()
    other = (df['race'] == 'Other').sum()
    race_count = pd.Series([white, black, asian, amer, other], 
                           index=['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'], 
                           dtype=float)
    
    avg_men_age = df[df['sex'] == 'Male']['age'].mean()

    all_data_education = (df['education']).count()
    bachelors = (((df['education'] == 'Bachelors').sum())/all_data_education)*100

    adv_edu_s = ((df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')).sum()
    adv_edu = df['education'].isin(['Bachelors','Masters','Doctorate']).sum()
    adv_edu_s_per = (adv_edu_s/adv_edu)*100
    no_adv_edu = (~(df['education'].isin(['Bachelors','Masters','Doctorate']))).sum()
    no_adv_edu_s = ((~(df['education'].isin(['Bachelors','Masters','Doctorate']))) 
                    & (df['salary'] == '>50K')).sum()
    no_adv_edu_s_p = (no_adv_edu_s/no_adv_edu)*100

    min_hrs_week = (df['hours-per-week']).min()

    min_hrs_50k = (((df['hours-per-week'] == min_hrs_week) & (df['salary'] == '>50K'))).sum()
    min_hrs_50kper = ((min_hrs_50k).sum()/(df['hours-per-week'] == min_hrs_week).sum())*100

    c_count = {}
    for i in df['native-country'].unique():
        count = ((df['native-country'] == i) & (df['salary'] == '>50K')).sum()
        c_count[i] = count
    c_count = pd.Series(c_count)
    max_idx = (c_count).idxmax()
    max_count = (c_count).max()
    t_count = c_count.sum()
    p_max_ccount = (max_count/t_count)*100
    
    india_s = ((df['native-country'].isin(['India'])) & (df['salary'] == '>50K'))
    india_s_occupation = (df[india_s].value_counts('occupation')).idxmax()
    india_s_occupation_n = (df[india_s].value_counts('occupation')).max()
    
    print(f'Race count: \n{race_count}')
    print(f'\nAverage age of men: \n{avg_men_age}')
    print(f'\nPercentage of people with a bachelor degree: \n{bachelors:.2f}%')
    print(f'\nPeople without advanced education: \n{no_adv_edu_s_p:.2f}%')
    print(f'\nPeople without advanced education who earns more than 50K: \n{no_adv_edu_s_p:.2f}%')
    print(f'\nMinimum hours per week: \n{min_hrs_week}')
    print(f'\nPeople who works the minimum hours with a salary more than 50K: \n{min_hrs_50kper}%')
    print(f'\nCountry with the highest percentage of people that earn >50K: \n{max_idx}: {p_max_ccount:.2f}%')
    print(f'\nMost popular occupation in India with >50K salary: \n{india_s_occupation}: {india_s_occupation_n}')

x = calculate_demografic_data()
print(x)