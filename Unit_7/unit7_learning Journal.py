# created a dictionary with list as values
stocks = {'AMD': [28.26, 32.02], 'AAPL': [196.48, 200.00],
          'FB': [200.00, 190.00], 'AMAZ': [1786.00, 1800.00],
          'SPOT': [149.00, 200.00], 'DlS': [136.78, 130.34]}

id = {'Director': ['Stanley Kubrick', 'Ridley Scott', 'James Cameron', 'Quentin Tarantino', 'Christopher Nolan',
                   'Alejandro Gonzalez Inarritu', 'Clint Eastwood', 'Mel Gibson', 'Steven Spielberg'],
      'Writer': ['Stanley Kubrick', 'Steven Spielberg', 'Christopher Nolan', 'Ethan Coen', 'Oliver Stone'],
      'Producer': ['Steven Spielberg', 'Clint Eastwood', 'Joel Coen', 'Ridley Scott', 'James Cameron',
                   'Stanley Kubrick'],
      'Actor': ['Al Pacino', 'Robert De Niro', 'Tom Hanks', 'Clint Eastwood', 'Mel Gibson', 'Quentin Tarantino',
                'Leonardo DiCaprio', 'Morgan Freeman'],
      'DocumentaryNarrator': ['Morgan Freeman', 'Tom Hanks', 'David Attenborough', 'James Earl Jones']}


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

# file1 = open("myfile.txt","w")
import json

with open("myfile.json", "w") as fp:
    json.dump(stocks, fp)

# file= open()