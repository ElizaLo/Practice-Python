project_twitter_data = open('project_twitter_data.csv', 'r')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for i in word:
        if i in punctuation_chars:
            word = word.replace(i, '')
    return word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(string):
    count = 0
    words = string.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            count += 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(string):
    count = 0
    words = string.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            count += 1
    return count

with open('resulting_data.csv', 'w') as res_data:
    res_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    res_data.write('\n')

    project_t_d = project_twitter_data.readlines()
    project_t_d.pop(0)
    for line in project_t_d:
        list_t_d = line.strip().split(',')
        res_data.write('{},{},{},{},{}'.format(list_t_d[1], list_t_d[2], get_pos(list_t_d[0]),
                                            get_neg(list_t_d[0]), (get_pos(list_t_d[0]) -  get_neg(list_t_d[0]))))
        res_data.write('\n')

project_twitter_data.close()
