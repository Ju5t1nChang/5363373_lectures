"""Function"""
# Definition
def func_name ( <parameter expression>):
   <function body>
   <end expression>

# Call
func_name ( <parameter>)

# End Statement
return <output>
pass

"""Comprehension"""
# Create a list with all even integers from 0 to 1 million
evens = []
for x in range(1_000_000 + 1):
if x % 2 == 0:
evens.append(x)
print(evens[:10])

# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])

#Dictionary Comprehension
pairs = [
('a', 1),
('b', 2),
('c', 3),
]

dic.update({key:value}) for key, value in pairs #OR

dic = {}
dic.update({key: value})
for key, value in pairs

# List Comprehension
newlist = [exoression for item in iterable if condition == True]

# Dictionary Into List
dic = {'a': 1, 'b': 2, 'c': 3}
pairs = [(key,value) for key,value in dic.items()]

# Filtering
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]

"""Comprehension Summary/Tuple Comprehension"""
# Some data (list of tuples)
data = [
('a', 1),
('b', 2),
('c', 3),
]
# Create a dict comprehension
dic = {k:v for k, v in data}


# Create a list comprehension
lst = [(k, v) for k, v in data]


# Create a set comprehension
st = {k for k, v in data}

"""Modules"""
import <module name> as <module reference>

"""Window’s Directory"""
DIR1 = 'C:\\User\\Someone'
DIR2 = r'C:\User\Someone'

