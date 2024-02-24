print('Reverse string using Recursion')
def reverse(input):
    if len(input)==0:
        return
    temp = input[0]
    reverse(input[1:])
    print(temp,end='')

input_value= 'good communication skill'

print('Approach 1')
reverse(input_value)

def reverse_aproach_2(input,index,size):
    if index == size:
        return
    temp = input[index]
    reverse_aproach_2(input,index+1,size)
    print(temp,end='')

size = len(input_value)
print('Approach 2')
reverse_aproach_2(input_value,0,size)






