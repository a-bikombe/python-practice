my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

# indexing
print(my_tuple[0])
# splicing
print(my_tuple[3:5])

print(len(my_tuple)) 

#returns index as value
print(my_tuple.index('abc'))
print(my_tuple.index(789))

# max()
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
my_tuple = ('abc', 'def', 'ghi', 'jkl')
max(my_tuple) # returns jkl
my_tuple = ('abc', 234, 567, 'def')
# max(my_tuple) would throw an error! cannot do both string and int

my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('abc', 'def', 'ghi', 'jkl')
min(my_tuple) # returns abc
my_tuple = ('abc', 234, 567, 'def')
# min(my_tuple) would throw an error! cannot do both string and int