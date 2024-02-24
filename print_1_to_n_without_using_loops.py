def show_number_sequence(number):
    if number>=1:
        show_number_sequence(number-1)
        print(number,end=' ')

if __name__ =='__main__':
    print('* Number sequence are *')
    show_number_sequence(10)