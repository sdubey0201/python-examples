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
print('')
print('Approach 2')
reverse_aproach_2(input_value,0,size)

# ********************* approach 3 ********************************
def get_reverse_string(input,size):
    if size<1:
        return
    if size ==1:
        return input[0]
    return input[size-1]+get_reverse_string(input,size-1)

if __name__ == "__main__":
    print('')
    print('Approch 3')
    input_str = 'Communication'
    size = len(input_str)
    print(get_reverse_string(input_str,size))








