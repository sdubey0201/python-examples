# Mean of array using recursion
# Input : 1 2 3 4 5
# Output : 3

# Input : 1 2 3
# Output : 2

def getMean():
    value = [1,2,3,4,5]
    index = len(value)-1
    sum = 0
    
    a = get_mean_value(value,index,sum)
    print('***result***')
    print(a)

def  get_mean_value(value,index,sum):
    if(index>=0):
        sum=sum+value[index]
        print(index)
        print(sum,end=' ')
        # pdb.set_trace()
        return get_mean_value(value,index-1,sum)
    else:
        # pdb.set_trace()
        result =sum/len(value)
        print(result)
        return result
import pdb
if __name__ =='__main__':
    print('* Number sequence are *')
    # show_number_sequence(10)
    # show_sequence_n_to_one(10)
    getMean()