intro = "My name is Jeff!"

# len()
intro2 = "Hello all!"
intro3 = "Hi there."
len(intro) # evaluates 16
len(intro2) # evaluates 10
len(intro3) # evaluates 9

# str.lower(), str.upper(), str.title()
print(intro.lower()) # prints 'my name is jeff!'
print(intro.upper()) # prints 'MY NAME IS JEFF!'
print(intro.title()) # prints 'My Name Is Jeff!'

# str.split()
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']