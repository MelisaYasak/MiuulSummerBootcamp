# Task 1
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

# Task 2

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

# Step 3:
print("Step 3: ", lst[:4])

#Step 4:
lst.pop(8)

# Step 5:
lst.append("M")

# Step 6: 
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

# Step 3:
dict["Daisy"][1] = 13

# Step 4: 
dict['Ahmet'] = ['Turkey', 24]
print(dict)

# Step 5:
dict.pop('Antonio')
print(dict)


#Task 5:
l = [2, 13, 18, 93, 22]

def func(l):
  odd_list = [element for element in l if element % 2 != 0]
  even_list = [element for element in l if element % 2 == 0]
  return even_list, odd_list

even_list, odd_list = func(l)

# Task 6: