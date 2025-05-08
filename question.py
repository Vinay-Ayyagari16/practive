#Find the sum of all elements in the list using sum()
numbers = [5, 2, 9, 1, 7]

# 1. Find the sum of all elements
total = sum(numbers)
print("Sum of elements:", total)

#sort the list in ascending order using sorted()
sorted_list = sorted(numbers)
print("Sorted list:", sorted_list)

#find the index of a specific element using index()
index_of_9 = numbers.index(9)
print("Index of 9:", index_of_9)

#Write a function to reverse the list without using reverse() or slicing ([::-1])
#Write a function to count the frequency of a specific element in the list

# Function to reverse a list without using reverse() or slicing
def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)  # Insert at the beginning
    return reversed_list

# Function to count frequency of a specific element
def count_frequency(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5]
print("Original List:", my_list)

# Reverse the list
reversed_result = reverse_list(my_list)
print("Reversed List:", reversed_result)

# Count frequency of 2
frequency = count_frequency(my_list, 2)
print("Frequency of 2:", frequency)

#Get a list of all keys using keys()
#Get the maximum score using max()
#Remove an item using pop()
