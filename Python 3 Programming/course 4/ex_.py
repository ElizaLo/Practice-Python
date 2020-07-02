'''
Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2,
which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10.
Save this instance to a variable t.
'''
class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t = NumberSet(6, 10)


'''
Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: 
arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
'''
class Animal:

    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs


spider = Animal(4,4)
spidlimbs = spider.limbs()


'''
Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables 
in the constructor: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: 
“[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name c1, 
assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, 
assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3. 
Practice printing both!
'''
class Cereal():

    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = int(fiber)

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)


'''
Below, we have provided a list of tuples that consist of student names, final exam scores, and whether or not they 
will pass the class. For some students, the tuple does not have a third element because it is unknown whether or not 
they will pass. Currently, the for loop does not work. Add a try/except clause so the code runs without an error - if 
there is no third element in the tuple, no changes should be made to the dictionary.
'''
students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except:
        #continue
        pass


'''
Below, we have provided code that does not run. Add a try/except clause so the code runs without errors. 
If an element is not able to undergo the addition operation, the string ‘Error’ should be appended to plus_four.
'''
nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num+4)
    except:
        plus_four.append('Error')


'''

'''
