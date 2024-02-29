def sum_of_array_element_using_recursion(element,lenth):
     
    if lenth<1:
        return 0
    sum = element[lenth-1]+sum_of_array_element_using_recursion(element,lenth-1)
    return sum

if __name__ == '__main__':
    element =[1, 2, 3, 4, 5]
    length = len(element)
    print(sum_of_array_element_using_recursion(element,length))
    # sum_of_array_element_using_recursion(element,length)

