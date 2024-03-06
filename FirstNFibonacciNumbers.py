def find_nth_fibonacci_number(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return find_nth_fibonacci_number(number-2)+find_nth_fibonacci_number(number-1)

def find_firstN_febonacci_number(input):
    for i in range(0,input):
        print(find_nth_fibonacci_number(i),end=" ")

if __name__ == '__main__':
    input = 7
    find_firstN_febonacci_number(input)