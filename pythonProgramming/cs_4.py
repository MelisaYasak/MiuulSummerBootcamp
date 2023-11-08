# -*- coding: utf-8 -*-
# Task 1: Read the file persona.csv and show general information about the data set.
import pandas as pd

persona = pd.read_csv("/content/drive/MyDrive/denmemiuul/persona.csv")
persona.head()

# Question 2: How many unique SOURCEs are there? What is their frequency?
print(f"Count of unique sources: {persona['SOURCE'].nunique()}")
print(f"Their frequency:\n{persona['SOURCE'].value_counts()}")

# Question 3: How many unique PRICEs are there?
print(f"Count of unique PRICE: {persona['PRICE'].nunique()}")

# Question 4: How many sales were realised at which PRICE?
print(f"PRICE frequnecy: \n{persona['PRICE'].value_counts()}")

# Question 5: How many sales from which country?
print(f"COUNTRY frequnecy: \n {persona['COUNTRY'].value_counts()}")

# Question 6: How much was earned from sales by country?
print(persona.groupby(['COUNTRY'])['PRICE'].agg(['sum']))

# Question 7: What is the number of sales by SOURCE types?

# Question 8: What are the PRICE averages by country?
print(persona.groupby(['COUNTRY'])['PRICE'].agg(['mean']))

# Question 9: What are the PRICE averages by SOURCEs?
print(persona.groupby(['SOURCE'])['PRICE'].agg(['mean']))

# Question 10: What are the PRICE averages by COUNTRY-SOURCE?
print(persona.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean())

# Task 2: What are the average earnings by COUNTRY, SOURCE, SEX, AGE?
result = persona.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean()
print(result)

# Task 3: Sort the output by PRICE.
agg_df = result.sort_values(ascending=False)
print(agg_df)

# Task 4: Convert the names in the index into variable names.
reset_ind_df = agg_df.reset_index()
print(reset_ind_df)

# Task 5: Convert age into a categorical variable and add it to agg_df.
age_groups = {
    (0, 18): '0_18',
    (19, 23): '19_23',
    (24, 30): '24_30',
    (31, 40): '31_40',
    (41, 70): '41_70'
}

reset_ind_df['AGE_CAT'] = reset_ind_df['AGE'].apply(
    lambda age: next((
        category for group, category in age_groups.items() if age in range(group[0], group[1] + 1)), None))
print(reset_ind_df)

# Task 6: Define new level-based customers (persona).
reset_ind_df['costumers_level_based'] = [f"{country.upper()}_{source.upper()}_{sex.upper()}_{age_cat.upper()}" for country, source, sex, age_cat in zip(reset_ind_df['COUNTRY'], reset_ind_df['SOURCE'], reset_ind_df['SEX'], reset_ind_df['AGE_CAT'] )]
print(reset_ind_df)

