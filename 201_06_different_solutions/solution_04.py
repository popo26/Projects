'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []


for tup in list(unsorted_list):
    #Ai woudl add print(tup) to see the current tup
    current_min = unsorted_list[0][1]
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            #swapping the index for minimum number
            current_min = unsorted_list[i][1]
            index = i
    #Ai: appending a minimum number in order to sorted_list
    sorted_list.append(unsorted_list[index])
    #Ai: eliminating a choice of numbers from smaller number that was added to the sorted_list at Line24
    unsorted_list.remove(unsorted_list[index])

print(unsorted_list)
print(sorted_list)
