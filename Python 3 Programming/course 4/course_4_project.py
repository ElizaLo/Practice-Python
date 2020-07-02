import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here

class WOFPlayer():

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):

    def __init__(self,name):
        WOFPlayer.__init__(self,name)

    def getMove(self, category, obscuredPhrase, guessed):
        user_input = input("Please Enter a move:")
        prompt = '''        
        {} has ${}
        Category: {}
        Phrase:  {}
        Guessed: {}
        Guess a letter, phrase, or type 'exit' or 'pass':
        '''.format(self.name, self.prizeMoney, self.Category, self.obscuredPhrase, self.guessed)
        print(prompt)
        return user_input


# Write the WOFComputerPlayer class definition (part C) here

def all_vowels(lst):
    for letter in lst:
        if letter not in VOWELS:
            return False
        else:
            continue
    return True

class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):

        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        r_number = random.randint(1, 10)
        if r_number > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self,guessed):
        
        available_letters = []
        
        for letter in LETTERS:
            if letter in guessed:
                continue
            elif letter not in guessed:
                if (letter in VOWELS) and (self.prizeMoney > VOWEL_COST):
                    available_letters.append(letter)
                elif letter not in VOWELS:
                    available_letters.append(letter)
                    
        return available_letters

    def getMove(self,category, obscuredPhrase, guessed):
        
        available_letters = self.getPossibleLetters(guessed)
        
        if len(available_letters) == 0:
            return 'pass'
        elif (all_vowels(available_letters)==True) and (self.prizeMoney < VOWEL_COST):
            return 'pass'
        else:
            if self.smartCoinFlip() == True:
                for i in range(len(self.SORTED_FREQUENCIES)):
                    letter = self.SORTED_FREQUENCIES[i]
                    if letter in available_letters:
                        return letter
            else:
                return random.choice(available_letters)
