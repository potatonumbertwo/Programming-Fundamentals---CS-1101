'''
Part 1
'''
# Create a string that is a long series of words separated by spaces

words = 'superb excellent outstanding magnificent marvelous wonderful awesome fantastic fabulous brilliant terrfic'

# Turn the string into a list of words using split.
split_words = words.split()

# print(split_words)
'''
Output:
['superb', 'excellent', 'outstanding', 'magnificent', 'marvelous', 'wonderful', 
'awesome', 'fantastic', 'fabulous', 'brilliant', 'terrfic']
'''

# Delete three words from the list, but delete each one using a different kind of Python operation.
split_words.pop(2)

del split_words[-1]

split_words.remove('superb')

# print(split_words)
'''
output:
 ['excellent', 'magnificent', 'marvelous', 'wonderful', 
'awesome', 'fantastic', 'fabulous', 'brilliant']
'''

# Sort the list
split_words.sort()
# print(split_words)

'''
Output:
['awesome', 'brilliant', 'excellent', 'fabulous', 'fantastic', 
'magnificent', 'marvelous', 'wonderful']

'''

# Add new words to the list (three or more) using three different kinds of Python operation.
split_words.append('auspicious')
new_words = ['perfect', 'fine']
split_words.extend(new_words)
split_words.insert(0, 'exceptional ')

# print(split_words)
'''
Output:
['exceptional ', 'awesome', 'brilliant', 'excellent', 'fabulous', 
'fantastic', 'magnificent', 'marvelous', 'wonderful', 'auspicious', 'perfect', 'fine']

'''
# Turn the list of words back into a single string using join
delimiter = ' '
join_words = delimiter.join(split_words)

# Print the string
print(join_words)
'''
Output: exceptional  awesome brilliant excellent fabulous fantastic 
magnificent marvelous wonderful auspicious perfect fine

'''



# Part 2
# Provide your own examples of the following using Python lists
# Nested lists
numbers = [['a', 'b', 'c'], [1, 2, 3], [True, False, True], ['math', 'english', 'science']]  # Nested lists
print(numbers)
'''
output :
[['a', 'b', 'c'], [1, 2, 3], [True, False, True], ['math', 'english', 'science']]
'''

# The “*” operator

multiple_list = [1, 21, 31, 41]
two_times = multiple_list * 2
print(two_times)

'''
output:
[1, 21, 31, 41, 1, 21, 31, 41]
'''

# List slices
lists = [33, 44, 55, 66, 77, 88, 99, 22]
slice_list = lists[2:4]
print(slice_list)
'''
output:
[55, 66]
'''


# The “+=” operator

def accumulator(a):
    total = 0
    for i in a:
        total += i
    return total


accumulator_list = [1, 101, 201, 301, 401, 501, 601, 701]
print(accumulator(accumulator_list))
'''
output:
2808
'''


# A list filter

def remove_zero(t):
    res = []
    for i in t:
        if i == 0:
            t.remove(0)
    return res


filter_list = [2, 0, 4, 6, 0, 5, 0, 7, 0, 8, 0, 9, 0, 10, 3, 2, 6, 0]
remove_zero(filter_list)
print(filter_list)
'''
output:[2, 4, 6, 5, 7, 8, 9, 10, 3, 2, 6]
'''
# A list operation that is legal but does the "wrong" thing, not what the programmer expects

example_list = [5, 6, 3, 8, 9]

remove_five = example_list.remove(5)

print(remove_five)
'''
Output: None
'''



# Part3
# How do you feel about the aspect assessments and feedback you have received from your peers?
'''
There does't have comment requirment for the comment. Mostly there are only one sentence for the comment
 Additionally, I don't agree one of the suggestion that
'Having the comments on the same line as the code may prove to be confusing.'
Moreover, about the aspect 1 of unit 2 programming assignment, 
One of the peer comment 'The student implements the functions but only called "clear_screen",
I don't think he or she understands the rubric of the aspect 1.
'''
# How do you think your peers feel about the aspect assessments and feedback you provided them?
'''
I always feel excited to access peers' assignment on Thursday if there have one. 
Everyone has different answer for the programming assignment. 
I am eager to see what others idea and compare with mine to give them suggestion. 
I read their code carefully, and provide my suggestion rewrite the code letting them to try.
For me ,it is a super useful learning process.

'''
