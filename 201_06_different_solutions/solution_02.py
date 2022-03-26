'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#Ai: stripping index[1] of each tuple in the list to create a new list
value_list = []
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

#Ai: sorting the list by ascending order
print(value_list)
value_list.sort()

#Ai: appending each tuple into a blank list by referencing ascending order of value_list
for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)#No need to remove existing tuples from unsorted_list
            break # No need for using break

print(sorted_list)
