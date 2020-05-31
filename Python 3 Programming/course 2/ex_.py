'''
Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
'''
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = [x[2] for x in lst_tups]


'''
Below, we have provided a list of tuples. 
Write a for loop that saves the second element of each tuple into a list called seconds.
'''
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = [x[1] for x in tups]


'''
If you remember, the .items() dictionary method produces a sequence of tuples. 
Keeping this in mind, we have provided you a dictionary called pokemon. 
For every key value pair, append the key to the list p_names, and append the value to the list p_number. 
Do not use the .keys() or .values() methods.
'''
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for key, value in pokemon.items():
        p_names.append(key)
        p_number.append(value)

'''
The .items() method produces a sequence of key-value pair tuples. 
With this in mind, write code to create a list of keys from the dictionary track_medal_counts and 
assign the list to the variable name track_events. Do NOT use the .keys() method.
'''
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []
for key, values in track_medal_counts.items():
    track_events.append(key)

'''
You will be sorting the following list by each element’s second letter, a to z. 
Create a function to use when sorting, called second_let. 
It will take a string as input and return the second letter of that string. 
Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.
'''
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(st):
    return st[1]

sorted_by_second_let = sorted(ex_lst, key = second_let)

'''
Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, 
and returns only its last character. Use this function to sort the list nums by the last digit of each number, 
from highest to lowest, and save this as a new list called nums_sorted.
'''
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(st):
    return st[-1]

nums_sorted = sorted(nums, reverse = True, key = last_char)


'''
Once again, sort the list nums based on the last digit of each number from highest to lowest. 
However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.
'''
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(st):
    return st[-1]

nums_sorted_lambda = sorted(nums, reverse = True, key = lambda x: last_char(x))
