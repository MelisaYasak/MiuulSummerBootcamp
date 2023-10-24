# Task 1: Define the Titanic data set in the Seaborn library.
import seaborn as sns
import matplotlib.pyplot as plt 

titanic = sns.load_dataset('titanic')
print(titanic.head())

# Task 2: Find the number of male and female passengers in the Titanic data set.
kadin_sayisi = titanic[titanic['sex'] == 'female']['sex'].count()
erkek_sayisi = titanic[titanic['sex'] == 'male']['sex'].count()

print(f"Kadın yolcu sayısı: {kadin_sayisi}")
print(f"Erkek yolcu sayısı: {erkek_sayisi}")

# Task 3: Find the number of unique values for each column.
for c in titanic.columns:
  print(f"{c} kolonunun unique değerlerinin sayısı:  {titanic[c].nunique()}")

# Task 4: Task 4: Find the number of unique values of the variable pclass.
# Task 5: Find the number of unique values of pclass and parch variables.
print("Titanic veri setindeki pclass kolonunun unique değerlerinin sayısı: ", titanic["pclass"].nunique())
print("Titanic veri setindeki pclass kolonunun unique değerlerinin sayısı: ", titanic["parch"].nunique())

# Task 6: Check the type of the variable embarked. Change its type to category and check it again.
print(titanic["embarked"].dtype)
titanic["embarked"] = titanic["embarked"].astype("category")
print(titanic["embarked"].dtype)

# Task 7: Show all information for embarked with value C.
print(titanic[titanic["embarked"]== "C"])

# Task 8: Show all information for embarked without S.
print(titanic[titanic["embarked"] != "S"])

# Task 9: Show all information on passengers under 30 years of age and female passengers.
print(titanic[(titanic["age"] < 30) & (titanic["sex"] == "female")])

# Task 10: Show the information on passengers with a Fare of more than 500 or an age of more than 70 years.
print(titanic[(titanic["fare"] > 500) | (titanic["age"] > 70)])

# Task 11: Find the sum of the empty values in each variable.
for c in titanic.columns:
  print(f"{c.upper()} kolonunun boş değerinin toplamı {titanic[c].isnull().sum()}")

# Task 12: Remove the who variable from the dataframe.
print(titanic.columns)
titanic = titanic.drop("who", axis=1)
print(titanic.columns)

# Task 13: Fill the empty values in the deck variable with the most repetitive value (mode) of the deck variable.
print(titanic["deck"])
print(" The most recurring value of the deck variable: ", titanic["deck"].mode())
titanic["deck"].fillna(titanic["deck"].mode()[0], inplace=True)
print(titanic["deck"])

# Task 14: Fill the empty values in the age variable with the median of the age variable.
print("median of age variable: ", titanic["age"].median())
titanic["age"].fillna(titanic["age"].median(), inplace= True)
print(titanic["age"])

# Task 15: Find the sum, count, mean values of the survived variable in the breakdown of pclass and gender variables.
result = titanic.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean'])
print(result)

# Task 16: Write a function that will give 1 to those under 30 and 0 to those equal to or above 30. Create a variable named age_flag in titanic dataset using the function you wrote (use apply and lambda structures).
def age_flag(age):
    return 1 if age > 30 else 0

titanic['age_flag'] = titanic['age'].apply(lambda x: age_flag(x))
print(titanic[['age', 'age_flag']].head())

# Task 17: Define the Tips data set from the Seaborn library.
tips = sns.load_dataset("tips")
print(tips.head())

# Task 18: Find the sum, min, max and average of the total_bill values according to the categories (Dinner, Lunch) of the variable Time.
grouped = tips.groupby("time")["total_bill"]

total_sum = grouped.sum()
min_value = grouped.min()
max_value = grouped.max()
mean_value = grouped.mean()


print("Toplam Bill:")
print(total_sum)
print("\nMinimum Bill:")
print(min_value)
print("\nMaksimum Bill:")
print(max_value)
print("\nOrtalama Bill:")
print(mean_value)


# Task 19: Find the sum, min, max and average of total_bill values by days and time.
grouped = tips.groupby(["time","day"])["total_bill"]

total_sum = grouped.sum()
min_value = grouped.min()
max_value = grouped.max()
mean_value = grouped.mean()


print("Toplam Bill:")
print(total_sum)
print("\nMinimum Bill:")
print(min_value)
print("\nMaksimum Bill:")
print(max_value)
print("\nOrtalama Bill:")
print(mean_value)


# Task 20: Find the sum, min, max and average of the total_bill and type values for Lunch time and female customers by day.
grouped = tips[(tips["time"] == "Lunch") & (tips["sex"] == "Female" )].groupby("day")[["total_bill", "tip"]].agg(["sum", "min", "max", "mean"])
print(grouped)

# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10? (use loc)
result = tips.loc[(tips["size"]<3)&(tips['total_bill']>10)].mean()
print(result)

# Task 22: Create a new variable called total_bill_tip_sum. Give the sum of totalbill and type paid by each customer.
def calculate_total_bill_tip_sum(row):
  return row['total_bill'] + row['tip']

# Task 23: Sort the total_bill_tip_sum variable from largest to smallest and assign the first 30 people to a new dataframe.
sorted_total_bill_tip_sum = tips.sort_values(by = "total_bill_tip_sum", ascending=False)
top_thrity = sorted_total_bill_tip_sum.iloc[:,:30]