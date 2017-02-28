animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end

#==============




animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation

y_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2
    

#==============


start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
    
square_list.sort()
print square_list

#==============



# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents['Sloth']
print residents['Burmese Python']



#==============


enu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Shrunken head'] = 78.33
menu['Lady Fingers'] = 33.33
menu['Chilled Monkey Brain'] = 3.32



print "There are " + str(len(menu)) + " items on the menu."
print menu


#==============


# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Other'




print zoo_animals


#==============



inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = [ "seashell", "strange berry", "lint" ]
inventory['backpack'].sort()
inventory['backpack'].remove("dagger")
inventory['gold'] = inventory['gold'] + 50

#==============


webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for definition in webster:
    print webster[definition]


#==============


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0:
            total += prices[key]
            stock[key] = stock[key] - 1
    return total
    
#==============


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]
    




#================
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]


# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (homework * .1) + (quizzes * .3) + (tests * .6)
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
        
        
#================


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results = []
    for numbers in lists:
        for num in range(len(numbers)):
            results.append(numbers[num])
    return results




print flatten(n)




#=======================
#+++BATTLESHIP+++++

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col


for turn in range(4):
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    print "Turn ", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    print_board(board)
    if (turn == 3):
        print "Game Over"
        



#===================

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if (guess == random_number):
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose!"
        
    
#===================

# reverse function

def reverse(text):
    word = []
    mirror = []
    result = ""
    size = 0
    
    for c in text:
        word.append(c)
    
    size = len(word)
    while (size > 0):
        mirror.append(word[size-1])
        size = size - 1
    
    result = ''.join(mirror)
    return result


#======================
#anti_vowel

def anti_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    zvowels = "aeiou"
    word = ""
    result = ""

    result = text
    for v in zvowels:
        result = result.replace(v, '')
        result = result.replace(v.upper(), '')
    
#    for v in vowels:
#        text.replace(v, "")
        
#    for c in text:
#        word.append[c]
    return result        
    


#================
# scrabble score

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    total = 0
    for w in word:
        total = total + score[w.lower()]
    return total


#===========================
# censor

def censor(text, word):
    return text.replace(word, '*' * len(word))

#===========================

#count

def count(sequence, item):
    frequency = 0
    for number in sequence:
        if item == number:
            frequency += 1
    
    return frequency


#=============================

#median

def median(numbers):
    result = 0 
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        #[4,4,5,5] this should return a = 1
        a = int(length/2)-1   
        b = a + 1
        result = (numbers[a] + numbers[b])/2.0
    else:
        result = numbers[length/2]
    return result
    
    
#=============================

#Standard deviation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) **2
    return variance/len(scores)
    
def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)

print "Grades: ", print_grades(grades)
print "Sum: ", grades_sum(grades)
print "Average: ", grades_average(grades)
print "Variance: ", variance
print "STD Deviation:", grades_std_deviation(variance)

#===================================

#evens to 50

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

cubes_by_four = [i**3 for i in range(1,11) if i**3 % 4 == 0]
print cubes_by_four

#===============
#slicing

to_21 = [i for i in range(1,22)]
odds = to_21[::2]
middle_third = to_21[7:14:1]


#========================
#lambda functions

squares = [i**2 for i in range(1,11)]
print filter(lambda x: x <= 70 and x >= 30, squares)

threes_and_fives = [i for i in range(1,16) if i % 3 == 0 or i % 5 ==0]

#===================

#derived class

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)



#==================================

#Classes

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        return "This is a " +self.color + " " + self.model + " with " +str(self.mpg) + " MPG."

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.display_car()



#===============================





    


    
    





        