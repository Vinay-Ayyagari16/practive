# Write a function to reverse a string without using Python’s built-in reverse functions or slicing.
def reverse_string(s):
    result=""
    for char in s:
        result = char + result  # Prepend each character
        return result
original = "hello"
reversed_str = reverse_string(original)
print("Original:", original)
print("Reversed:", reversed_str)


# Write a function that checks if a given string is a palindrome (reads the same backward as forward).
def is_palindrome(s):
    length = len(s)
    for i in range(length//2):
        if s[i] != s[length -1 -i]:
            return False
        return True
print(is_palindrome("madam"))      
print(is_palindrome("racecar"))    
print(is_palindrome("hello"))    
print(is_palindrome("abba"))     
        

#Print numbers from 1 to 100. For multiples of 3, print “Fizz” instead of the number. For multiples of 5, print “Buzz”. For numbers which are multiples of both 3 and 5, print “FizzBuzz”.
def fizz_buzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
fizz_buzz()

#Write a recursive function to find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
number = 5
print("Factorial of", number, "is", factorial(number))


#Given a list of numbers, find and return the second largest number without using the built-in sort() or max() more than once.
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    largest = max(numbers)
    second = None
    for num in numbers:
        if num != largest:
            if second is None or num > second:
                second = num
                
    return second            
nums = [12, 5, 8, 20, 20, 10]
print("Second largest number is:", second_largest(nums))

# Write a function that counts the number of vowels and consonants in a given string.
def count_vowels_consonants(test):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in test:
        if char.isalpha:
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

text = "Hello, World!"
vowels,consonants = count_vowels_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)

#Write a function to merge two sorted lists into one sorted list without using built-in sort functions.
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    # Compare elements from both lists and add the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add remaining elements from list1
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Add remaining elements from list2
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Example usage
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print("Merged List:", merge_sorted_lists(a, b))

# Given a list of integers, return a list of duplicates
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 3]
print("Duplicates:", find_duplicates(numbers))

#Write a function that checks whether two strings are anagrams of each other.
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters are the same
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("listen", "silent"))      
print(are_anagrams("hello", "world"))       
print(are_anagrams("Dormitory", "Dirty room"))  

#Create a function that takes two numbers and an operator (+, -, *, /) and returns the result. Handle division by zero.
def basic_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

# Example usage
print(basic_calculator(10, 5, '+')) 
print(basic_calculator(10, 0, '/'))
print(basic_calculator(8, 2, '*')) 
print(basic_calculator(7, 3, '%'))   


