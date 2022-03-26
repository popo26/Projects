'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#Ai: loop unsorted_list to find a minimum number to create a new list(sorted_list) by removing a minimum number from unsorted_list each time it loops
for x in range(0, len(unsorted_list)):

    min = unsorted_list[0][1]
    print(min)
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])


print(unsorted_list)
print(sorted_list)
