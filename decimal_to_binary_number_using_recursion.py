def decimal_to_binary_using_recursion(decimal):
    if decimal == 0:
        return 0
    else:
        a = decimal%2
        b = int(decimal/2)
        c = a+10*decimal_to_binary_using_recursion(b)
        return c

if __name__ == '__main__':
    print(decimal_to_binary_using_recursion(10))
