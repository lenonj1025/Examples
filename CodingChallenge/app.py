

def is_unique(my_string):
    for i in range(len(my_string) - 1):
        for j in range(i + 1, len(my_string)):
            if my_string[i] == my_string[j]:
                return False

    return True

def is_unique_solution_using_set(my_string):
    my_set = set()
    for char in my_string:
        my_set.add(char)
    return len(my_set) == len(my_string)

def is_unique_solution_using_sorting(my_string):
    my_list_of_sorted_characters = sorted(my_string)
    for i in range(len(my_list_of_sorted_characters) - 1):
        if my_list_of_sorted_characters[i] == my_list_of_sorted_characters[i + 1]:
            return False

    return True

# Input: abc
# Expected Output: True
print(is_unique("abc"))

# Input: apple
# Expected Output: False
print(is_unique("apple"))

# Input: banana
# Expected Output: False
print(is_unique("banana"))

# Input: dog
# Expected Output: True
print(is_unique("dog"))
