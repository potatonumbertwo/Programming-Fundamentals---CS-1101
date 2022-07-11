# Part1
prefixes = 'JKLMNP'
names = 'OQ'
suff = 'uack'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)
for name in names:
    print(name + suff)
'''
output
Jack
Kack
Lack
Mack
Nack
Pack
Ouack
Quack
'''

# part 2
# Strings are immutable,which means we can;t change an existing string.
# for example

example1 = ' Good morning,Potato!'
example1[0] = 'Watermelon'
print(example1)

# output
# TypeError: 'str' object does not support item assignment

'''
If we want to change an element inside a string, we need to create a new string.
The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character,
including the first but excluding the last.

'''
slice_example1 = example1[1:13]
print(slice_example1)

# output :  Good morning

'''
if you omit the first index (before the colon),
the slice starts at the beginning of the string
'''

greeting_watermelon = example1[:14] + 'Watermelon!'
print(greeting_watermelon)

# output:  Good morning,Watermelon!

'''
If you omit the second index, the slice goes to the end of the string
'''
omit_example1 = example1[14:]
print(omit_example1)
# output : Potato!

'''
Slices the last string from  backwards will start from -1 
'''

greeting_rosie = example1[:14] + 'Rosie' + example1[-1]
print(greeting_rosie)
# output :  Good morning,Rosie!
'''
Slices fileNamesList the string
'''
greeting_potato = example1[:]
print(greeting_potato)
#  Good morning,Potato!
