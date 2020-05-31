'''
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
Find the total number of characters in the file and save to the variable num.
'''
file = open('travel_plans.txt', 'r')
num = len(file.read())


'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words.
'''
file = open('emotion_words.txt', 'r')
file = file.read().split()
num_words = len(file)


'''
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
'''
with open('school_prompt.txt', 'r') as f:
    num_lines = 0
    for line in f:
        num_lines += 1


'''
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''
with open('school_prompt.txt', 'r') as f:
    f = f.read()
    beginning_chars = f[:30]


'''
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''
with open('school_prompt.txt', 'r') as f:
    three = []
    for line in f:
        line = line.split()
        three.append(line[2])


'''
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
'''
with open('emotion_words.txt', 'r') as f:
    emotions = []
    for line in f:
        line = line.split()
        emotions.append(line[0])


'''
Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
'''
with open('travel_plans.txt', 'r') as f:
    f = f.read()
    first_chars = f[:33]


'''
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
'''
with open('school_prompt.txt', 'r') as f:
    p_words = []
    for word in f.read().split():
        if 'p' in word:
            p_words.append(word)
