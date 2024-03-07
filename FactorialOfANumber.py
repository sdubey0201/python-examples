def FactorialOfANumber(number):
    if number == 1:
        return 1
    return number* FactorialOfANumber(number-1)

if __name__ == '__main__':
    number = 3
    print(FactorialOfANumber(number))