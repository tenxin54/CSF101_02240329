import string
from collections import Counter

def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1) :
        if num % i ==0:
            return False
    return True
def sum_of_primes():
   first = int(input("Enter the first number:"))
   last = int(input("Enter the last number:"))
   sum = 0
   for i in range (first, last+1):
       if is_prime(i):
           sum+=i
   print(f"Sum of prime number:{sum}")

def meter_to_feet(meters):
    return meters * (16.4/5)
def feet_to_meter(feet):
    return feet / (16.4/5)

def length_converter():
    print("Length Converter")
    print("1. Meter to Feet")
    print("2. Feet to Meter")

    choice = input("Choose which unit you want to convert (M or F): ")

    if choice == 'M':
        meters = float(input("Length in meters you want to change in feet: "))
        feet = meter_to_feet(meters)
        print(f"{meters} meters is equal to {feet:.2f} feet.")
    elif choice == 'F':
        feet = float(input("Length in feet you want to change in meters : "))
        meters = feet_to_meter(feet)
        print(f"{feet} feet is equal to {meters:.2f} meters.")
    else:
        print("Invalid choice. Please select M or F.")

def consonent_counter():
    string = input("Write your beautiful thoughts:")
    non_vowel = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    consonents = 0
    for char in string:
            if char in non_vowel:
                 consonents += 1
    print(f"Number of consonants: {consonents}")

def min_max():
    num_want = int(input("How many numbers do you want to enter? "))
    digits = []
    for i in range(num_want):
        num = float(input(f"Enter number {i + 1}: "))
        digits.append(num)

    if digits:
        print(f"Minimum number: {min(digits)}")
        print(f"Maximum number: {max(digits)}")
    else:
        print("No numbers were entered.")

def palindrome():
    anything=input("What is in your mind:")

    if anything == anything[::-1]:
        print("It consists of palindrome.")
    else:
        print("It does not consists of palindrome.")

def word_counter():
    text_reader = input("Enter the file name (with .txt extension): ")
    given = open(text_reader, 'r')
    txt = given.read()
    given.close()
    txt = txt.lower()  
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    words = txt.split()
    word_count = len(words)
    print(f"Total number of words: {word_count}")
    word_frequencies = Counter(words)
    specific_words = ["the", "and", "was"]
    for word in specific_words:
        print(f"'{word}' occurs {word_frequencies[word]} times.")

while True:
    print("select a function (1-6): \n1. Calculate the sum of prime numbers \n2. Convert length units \n3. Count consonents in string \n4. Find min and max numbers \n5. Check for palindrome \n6. Word counter \n0. Exit program ")
    choose = int(input("Enter your choice:"))

    if choose == 1:
        sum_of_primes()

    elif choose == 2:
        length_converter()

    elif choose == 3:
        consonent_counter()

    elif choose == 4:
        min_max()

    elif choose == 5:
        palindrome()
    
    elif choose == 6:
        word_counter()

    elif choose == 0:
        print("Thank You!", "Hope you enjoyed it")
        break

    else:
        print("Invalid choice. Please choose the valid choice from 1-6 and choose 0 to exit")


