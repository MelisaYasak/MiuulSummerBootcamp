# Task 1: To analyse the data structures of variables
x = 8
print(type(x)) # <class 'int'>

y = 3.2
print(type(y)) # <class 'float'>

z = 8j + 18 
print(type(z)) # <class 'complex'>

a = "Hello World"
print(type(a)) # <class 'str'>

b = True
print(type(b)) # <class 'bool'>

c = 23 < 22
print(type(c)) # <class 'bool'>

l = [1,2,3,4]
print(type(l)) # <class 'list'>

d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
print(type(d)) # <class 'dict'>

t = ("Machine Learning", "Data Science")
print(type(t)) # <class 'tuple'>

s = {"Python", "Machine Learning", "Data Science"}
print(type(s)) # <class 'set'>

# Task 2: Capitalise all letters of the given string expression. Replace comma and period with space, word by word.
text = "The goal is to turn data into information, and information into insight."
words = text.split()
uppercase_words = [word.upper() for word in words if word.isalpha()]
print(uppercase_words) # ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'AND', 'INFORMATION', 'INTO']

# Task 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Step 1:
print("Step 1: Length of list: ", len(lst))

# Step 2:
print("Step 2: The element at the zeroth index is:", lst[0], "\nThe element at the tenth index is:", lst[10])

# Step 3: Create a list ["D", "A", "T", "A"] from the given list. 
print("Step 3: ", lst[:4])

#Step 4: Delete the element in the eighth index.
lst.pop(8)

# Step 5: Add a new element.
lst.append("M")

# Step 6: Add the "N" element to the eighth index again
lst.insert(8, "N")

# Task 4

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Step 1:
print("KEYS", dict.keys())

# Step 2:
print("Values", print(dict.values()))

# Step 3: Update the 12 value of the Daisy key to 13
dict["Daisy"][1] = 13

# Step 4: Add a new value with key value Ahmet and value value [Turkey,24].
dict['Ahmet'] = ['Turkey', 24]
print(dict)

# Step 5: Delete Antonio from the dictionary
dict.pop('Antonio')
print(dict)


#Task 5: Write a function that takes a list as argument, assigns the odd and even numbers in the list to separate lists and returns these lists
l = [2, 13, 18, 93, 22]

def func(l):
  odd_list = [element for element in l if element % 2 != 0]
  even_list = [element for element in l if element % 2 == 0]
  return even_list, odd_list

even_list, odd_list = func(l)

# Task 6: Print student degrees by faculty using Enumarate

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
muhendislik_dereceleri = ogrenciler[:3]  
tip_dereceleri = ogrenciler[-3:]  

for i, ogrenci in enumerate(muhendislik_dereceleri, start=1):
    print(f"Mühendislik Fakültesi {i}. öğrenci: {ogrenci}")

for i, ogrenci in enumerate(tip_dereceleri, start=1):
    print(f"Tıp Fakültesi {i}. öğrenci: {ogrenci}")


# Task 7: Print course information using zip
ders_kodu = ["CMP1005", "PSY10001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30, 75, 150, 25]

liste =set(zip(kredi, ders_kodu, kontenjan))
for l in liste:
  print(f"Kredisi {l[0]} olan {l[1]} kodlu dersin kontenjanı {l[2]} kişidir.")

# Task 8: If kume1 includes kume2, you are expected to define the function that will print the common elements of kume2 if it does not include kume1.

kume1 = set(["data", "python"])
kume2 = set(["data","function", "qcut", "lambda", "python", "miuul"])
if kume1.issuperset(kume2):
  print(kume1.intersection(kume2))
else:
  print(kume2.difference(kume1)) # {'lambda', 'function', 'miuul', 'qcut'} 


