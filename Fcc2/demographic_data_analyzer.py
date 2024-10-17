import pandas as pd

def demographic_data_analyzer(df):
    # 1. How many people of each race are represented in this dataset?
    race_counts = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    bachelors_percentage = round((df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earning_advanced = round((len(advanced_edu[advanced_edu['salary'] == '>50K']) / len(advanced_edu)) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    non_advanced_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earning_non_advanced = round((len(non_advanced_edu[non_advanced_edu['salary'] == '>50K']) / len(non_advanced_edu)) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_high_earning = df[df['hours-per-week'] == min_hours_per_week]
    percentage_high_earning_min_hours = round((len(min_hours_high_earning[min_hours_high_earning['salary'] == '>50K']) / len(min_hours_high_earning)) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_high_earning = df.groupby('native-country').apply(lambda x: (x['salary'] == '>50K').mean() * 100)
    highest_country = country_high_earning.idxmax()
    highest_percentage = round(country_high_earning.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_high_earning = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation = india_high_earning['occupation'].mode()[0]

    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'bachelors_percentage': bachelors_percentage,
        'percentage_high_earning_advanced': percentage_high_earning_advanced,
        'percentage_high_earning_non_advanced': percentage_high_earning_non_advanced,
        'min_hours_per_week': min_hours_per_week,
        'percentage_high_earning_min_hours': percentage_high_earning_min_hours,
        'highest_country': highest_country,
        'highest_percentage': highest_percentage,
        'most_popular_occupation': most_popular_occupation,
    }
