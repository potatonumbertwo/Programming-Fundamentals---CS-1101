# 11.2
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# print(histogram('potato'))


# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# >>> for k, v in knights.items():
# ...     print(k, v)

'''
# 11.3 Looping and dictionaries
def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('potato')
# print_hist(h)

for key in sorted(h):  # sorted order
    print(key, h[key])




# 11.4 Reverse lookup
def reverse_lookup(d, v):  # search pattern
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()  # built-in exception it can take a detail error message


word = histogram('potato')
key = reverse_lookup(word, 2)
print(key)
'''
# 11.5 Dictionaries and lists


# 12.5 Lists and tuples
'''
Tuple can be useful with loops over list because zip function returns a list of tuple
each tuple can contain a element corresponding with another element from the lists
'''

items = ['potato', 'apple pair', 'banana', 'steak']
prices = [0.99, 2.45, 0.45, 6.78]
discount = [0, 0.45, 0, 0.8]


def zip_example():
    for i in zip(items, prices, discount):
        print(i)


zip_example()

'''
Output:
('potato', 0.99, 0)
('apple pair', 2.45, 0.45)
('banana', 0.45, 0)
('steak', 6.78, 0.8)
'''


def enumerate_example():
    for index, element in enumerate(items):
        print(index, element)


enumerate_example()

'''
Output: 
0 potato
1 apple pair
2 banana
3 steak

The result from enumerate is an enumerate object, 
which iterates a sequence of pairs; 
each pair contains an index (starting from 0) 
and an element from the given sequence
'''

'''
Dictionaries have a method called items that returns a sequence of tuples, 
where each tuple is a key-value pair.
'''


def items_example():
    for key, value in grades.items():
        print(key, value)


grades = {'math': 99, 'english': 90, 'science': 95, 'physics': 100, 'chemistry': 3}

items_example()

'''
Output:
math 99
english 90
science 95
physics 100
chemistry 3
'''
