#List Operations
nums = [5, 2, 9, 1, 5, 6]

# Built-in Functions
print("Sum:", sum(nums))
print("Sorted:", sorted(nums))
print("Index of 9:", nums.index(9))

#Without Built-in Functions
def reverse_list(lst):

    result = []
    for i in range(len(lst)-1, -1, -1):  # Starts from the last index to the first
        result.append(lst[i])            # Adds each element to a new list
    return result                        # Returns the reversed list

def count_frequency(lst, value):
    count = 0
    for item in lst:             # Iterates through each element
        if item == value:        # Checks if it matches the target value
            count += 1           # Increments the counter
    return count                 # Returns the final count

# print("Reversed List:", reverse_list(nums))
print("Frequency of 5:", count_frequency(nums, 5))


# Dictionary Operations
students = {'Alice': 85, 'Bob': 78, 'Charlie': 92}

# Built-in Functions
print("Keys:", list(students.keys()))
print("Max Score:", min(students.values()))
print("Pop 'Bob':", students.pop('Bob'))

# Without Built-in Functions
def average_score(d):
    total = 0
    count = 0
    for score in d.values():
        total += score
        count += 1
    return total / count if count else 0

def student_with_min_score(d):
    min_score = None
    student_name = None
    for name, score in d.items():
        if min_score is None or score < min_score:
            min_score = score
            student_name = name
    return student_name

print("Average Score:", average_score(students))
print("Student with Min Score:", student_with_min_score(students))


# Tuple Operations
t = (3, 5, 7, 2, 8)

# Built-in Functions
print("Length:", len(t))
print("Max Value:", max(t))
print("As List:", list(t))

# Without Built-in Functions
def product_of_elements(tup):
    product = 1
    for num in tup:
        product *= num
    return product

def second_largest(tup):
    first = second = float('-inf')
    for num in tup:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

print("Product of Elements:", product_of_elements(t))
print("Second Largest:", second_largest(t))


# Set Operations
s = {1, 2, 3, 4}

# Built-in Functions
s.add(5)
print("After Add:", s)
print("Union with {3,4,5,6}:", s.union({3, 4, 5, 6}))
print("Is 3 in set:", 3 in s)

# Without Built-in Functions
def intersection_set(set1, set2):
    result = set()  # Create an empty set to store common elements
    for item in set1:  # Iterate over each element in set1
        if item in set2:  # Check if the item is also in set2
            result.add(item)  # If so, add it to result
    return result  # Return the result set


def is_subset(subset, superset):
    for item in subset:  # Go through each element in the subset
        if item not in superset:  # If any item is missing in superset
            return False  # It's not a subset
    return True  # All items found; it's a subset


print("Intersection with {4,5,6}:", intersection_set(s, {4, 5, 6}))
print("Is {1,2} subset of s:", is_subset({1, 2}, s))
