def lengthOfAStringUsingRecursion(input) -> int :
    if input == '':
        return 0
    return lengthOfAStringUsingRecursion(input[1:])+1

if __name__ == '__main__':
    print('length of String using recursion ')
    input1 = ''
    input2 = 'test'
    input3 = 'python code'
    print(lengthOfAStringUsingRecursion(input1))
    print(lengthOfAStringUsingRecursion(input2))
    print(lengthOfAStringUsingRecursion(input3))