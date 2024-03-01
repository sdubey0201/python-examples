def reverseOfStringUsingRecursion(input,length):
    if length<=0:
        return ''
    result = input[length-1]+reverseOfStringUsingRecursion(input,length-1)
    return result

if __name__ == '__main__':
    input = 'Communication'
    length = len(input)
    print(reverseOfStringUsingRecursion(input,length))