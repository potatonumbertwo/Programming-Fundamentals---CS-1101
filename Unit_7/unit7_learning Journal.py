# created a dictionary with list as values
stocks = {'AMD': [28.26, 32.02], 'AAPL': [196.48, 200.00],
          'FB': [184.68, 190.00], 'AMAZ': [1786.00, 1800.00],
          'SPOT': [149.00, 156.35], 'DlS': [136.78, 130.34]}


def invert_dict(dictionary):
    """to turn each of the list items into separate keys and return a new dict"""
    returned_dict = dict()
    key_list = dictionary.keys()
    for key in key_list:
        old_values = dictionary.get(key)
        for new_key in old_values:
            returned_dict[new_key] = key
    return returned_dict


print(invert_dict(stocks))



# {28.26: 'AMD', 32.02: 'AMD', 196.48: 'AAPL', 200.0: 'AAPL',
# 184.68: 'FB', 190.0: 'FB', 1786.0: 'AMAZ', 1800.0: 'AMAZ',
# 149.0: 'SPOT', 156.35: 'SPOT', 136.78: 'DlS', 130.34: 'DlS'}


# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse
#
#
# print(invert_dict(stacks))
