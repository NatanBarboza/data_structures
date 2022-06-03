from random import randrange

def duplicate_nums(array):
    duplicates = []
    
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                duplicates.append(array[j])
            else:
                continue
    
    return print(f"The duplicates itens are {duplicates}")

def reversed_array(array):
    begin = 0
    end = len(array) - 1

    while(begin < end):
        array[begin], array[end] = array[end], array[begin]
        begin += 1
        end -= 1

    return print(f"The reversed list are {array}")


if(__name__ == "__main__"):
    array = []
    while(True):
        if(len(array) == 10):
            break
        array.append(randrange(0, 100))

    print(array)      #initial values

    duplicate_nums(array)               #changed values -> duplicate

    reversed_array(array)                #changed values -> reversed