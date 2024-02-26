# Sum of natural numbers using recursion
# Input : 3
# Output : 6
# Explanation : 1 + 2 + 3 = 6

# Input : 5
# Output : 15
# Explanation : 1 + 2 + 3 + 4 + 5 = 15

def sum_of_natural_numbers_using_recursion(value):
    if value<=1:
        return value
    else:
        return value+sum_of_natural_numbers_using_recursion(value-1)

if __name__ == '__main__':
    print(sum_of_natural_numbers_using_recursion(5))