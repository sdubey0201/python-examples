print('hello world')
def reverse(input):
    if len(input)==0:
        return
    temp = input[0]
    reverse(input[1:])
    print(temp,end='')

input_value= 'good communication skill'
reverse(input_value)


