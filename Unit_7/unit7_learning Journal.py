import pickle
import json

# created a dictionary with list as values
stocks = {'AMD': [28.26, 32.02], 'AAPL': [196.48, 200.00],
          'FB': [200.00, 190.00], 'AMAZ': [1786.00, 1800.00],
          'SPOT': [149.00, 200.00], 'DlS': [136.78, 130.34]}


def invert_dict(dictionary):
    """to turn each of the list items into separate keys and return a new dict"""
    returned_dict = dict()
    key_list = dictionary.keys()
    for key in key_list:
        old_values = dictionary.get(key)
        for new_key in old_values:
            returned_dict[new_key] = key
    return returned_dict


#
# with open("myfile.json", "w") as fp:
#     json_string = json.dump(stocks, fp)
#     print(json_string)
#
# pickle_file = open("myfile.txt", "w")
# dict_to_string = pickle.dumps(stocks)
#
# load_string = pickle.loads(dict_to_string)


def write_dict(dictionary, file_name):
    with open(file_name, 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_dict(file_name):
    with open(file_name, 'rb') as handle:
        load_handle = pickle.load(handle)
        print(load_handle)
        return load_handle


filename = 'stock_dict'
i = read_dict(filename)
inverted_stocks = invert_dict(stocks)
write_dict(inverted_stocks, filename)

# print(i == stocks)
