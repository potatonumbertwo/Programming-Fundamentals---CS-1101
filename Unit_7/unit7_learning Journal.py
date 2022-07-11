import pickle
import json

# created a dictionary with list as values
stocks = {'AMD': [28.26, 32.02], 'AAPL': [196.48, 200.00],
          'FB': [200.00, 190.00], 'AMAZ': [1786.00, 1800.00],
          'SPOT': [149.00, 200.00], 'DlS': [136.78, 130.34],
          'NASDAQ': [7773.94, 7869.52], 'BABA': [162.06, 160.55]}


def invert_dict(dictionary):
    """to turn each of the list items into separate keys and return a new dict"""
    returned_dict = dict()
    key_list = dictionary.keys()
    for key in key_list:
        old_values = dictionary.get(key)
        for new_key in old_values:
            returned_dict[new_key] = key
    return returned_dict


def write_dict(dictionary, file_name):
    with open(file_name, 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_dict(file_name):
    with open(file_name, 'rb') as handle:
        load_handle = pickle.load(handle)
        print(load_handle)
        return load_handle


write_dict(stocks, 'stock_input_file')

dict_was_read_in = read_dict('stock_input_file')

inverted_stocks = invert_dict(dict_was_read_in)

write_dict(inverted_stocks, 'stock_out_file')
