import random

def number () :
    min_number = int(input("what is the minimum number "))
    max_number = int(input("what is the maximum number "))
    print(random.randint(min_number, max_number))

number()


response = input("Again ? ")

while response == "yes" :
    number()
    response = input("again ? ")
    if response == "no":
        exit
