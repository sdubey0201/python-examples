def show_number_sequence(number):
    if number>=1:
        show_number_sequence(number-1)
        print(number,end=' ')
# Print N to 1 without loop
# Input: N = 5
# Output: 5 4 3 2 1
# Explanation: We have to print numbers from 5 to 1.

# Input: N = 10
# Output: 10 9 8 7 6 5 4 3 2 1
# Explanation: We have to print numbers from 10 to 1.

def show_sequence_n_to_one(number):
    if number>=1:
        print(number,end=' ')
        show_sequence_n_to_one(number-1)


if __name__ =='__main__':
    print('* Number sequence are *')
    # show_number_sequence(10)
    show_sequence_n_to_one(10)