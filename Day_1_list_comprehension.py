#1- Extract even numbers

nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
print(even)   # [2, 4, 6]

#-----------------------------------------

#2-Convert ints to “Even”/“Odd”

nums = range(1, 11)
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)

#-----------------------------------------------
#3- Multiply values with index

nums = [10, 20, 30, 40]
result = [v * i for i, v in enumerate(nums)]
print(result)   # [0, 20, 60, 120]

#----------------------------------------------

#4- Flatten 2D list

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6]

#----------------------------------------------

#5- Unique positives

nums = [-1, 2, 2, 3, -5, 3, 4]
unique_pos = list({x for x in nums if x > 0})
print(unique_pos)  # e.g. [2, 3, 4]

#---------------------------------------------------

#6-Strip whitespace & lower

raw = ["  Bank ", " Data", " ENGINEERING ", " Python "]
cleaned = [s.strip().lower() for s in raw]
print(cleaned)

#-----------------------------------------------------

#7- Replace None with 0

vals = [10, None, 5, None, 20]
fixed = [x if x is not None else 0 for x in vals]
print(fixed)  # [10, 0, 5, 0, 20]

#-------------------------------------------------------

#8 - Combine categories & items

categories = ["A", "B"]
values = [1, 2, 3]
cartesian = [(c, v) for c in categories for v in values]
print(cartesian)

#-----------------------------------------------------------

#9 - Extract dict values

records = [
    {"id": 1, "name": "Alice", "score": 90},
    {"id": 2, "name": "Bob", "score": 85}
]
names = [r["name"] for r in records]
print(names)  # ['Alice', 'Bob']

#----------------------------------------------------------

#9 - Only even squares

nums = range(10)
even_squares = [x*x for x in nums if x % 2 == 0]
print(even_squares)

#-----------------------------------------------------------

#10 - Count length by category

words = ["data", "python", "spark", "dbt", "aws"]
lengths = {w: len(w) for w in words}
print(lengths)


#------------------------------------------------------------









