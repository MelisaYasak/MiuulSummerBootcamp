# Task 1: Define the Titanic data set in the Seaborn library.
import seaborn as sns
import matplotlib.pyplot as plt 

titanic = sns. load_dataset('titanic')
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