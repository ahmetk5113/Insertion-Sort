def insertion_sort():
    # LOCAL VARIABLES
    unordered_list = [4,3,2,10,12,1,5,6]
    length = range(1,len(unordered_list))
    # LOGIC
    for value in length:
        value_to_sort = unordered_list[value]
        while unordered_list[value - 1] > value_to_sort and value > 0:
            unordered_list[value],unordered_list[value - 1] = unordered_list[value - 1],unordered_list[value]
            value = value - 1

    print(unordered_list)


    

insertion_sort()