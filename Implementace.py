'''
projekt_1.py: První projekt do Engeto Online Python Akademie
author: Iva Slažanská
email: ivaslazanska@gmail.com
discord: iv.0077
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob" : 123, "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
line = "-" * 40
while True:
    user_name = input("Please login. Enter your name: ")
    if user_name not in users:
        print(f"Wrong account. Please try again.")
    else:
        break

while True:
    password = input("Please enter your password: ")
    if not password:
        print(f"Wrong password. Please try again.")
    else:
        break

print(line)
if password == str(users.get(user_name)):
    print(f"Welcome to the app {user_name}")
else:
    print(f"Sorry, you are not registered. Terminating the program.")
    exit()

print(f"We have {len(TEXTS)} texts to be analyzed.")

print(line)
text = 0
while True:
    answer = input("Enter a number btw. 1 and 3 to select: ")
    if not answer:
        print(f"Wrong input. Please try again.") 
    else:
        break

if answer.isnumeric():
    answer = int(answer)
    if answer < 1 or answer > 3:
        print(f"{answer} is not btw. 1 and 3. Terminating the program.")
        exit()
    else:
        text = TEXTS[answer - 1]

else:
    print(f"{answer} incorrect answer. Terminating the program.")
    exit()

all_texts = text.split()
only_words = [word.strip(',.?!') for word in all_texts]
lenght_num = [len(word) for word in only_words]
title_case = [word for word in only_words if word.istitle() and word.isalpha()]
upper_case = [word for word in only_words if word.isupper() and word.isalpha()]
lower_case = [word for word in only_words if word.islower() and word.isalpha()]
numero = [word for word in only_words if word.isnumeric()]
together = [numero and title_case]
numero_int = [int(number) for number in numero]

print(line)
print(f"There are {len(all_texts)} words in the selected text.")
print(f"There are {len(together) + len(title_case)} titlecase words.")
print(f"There are {len(upper_case)} uppercase words.")
print(f"There are {len(lower_case)} lowercase words.")
print(f"There are {len(numero)} numeric strings.")
print(f"The sum of all the numbers {sum(numero_int)}.")

star = '*'
space = ' '
sequence = set(lenght_num)
frequency_numbers = []
for num in sequence:
    frequency_numbers.append(lenght_num.count(num))
highest_number = max(frequency_numbers)

print(line)
middle_text = "OCCURENCES"
mid_width = len(middle_text)

print(f"LEN | {middle_text:^{highest_number}} | NR.")

print(line)
for quantity in sorted(sequence):
    count_of_spaces = highest_number - lenght_num.count(quantity)
    print(f"{quantity:2}  | {star * lenght_num.count(quantity)}{space * count_of_spaces}   | {lenght_num.count(quantity)}")