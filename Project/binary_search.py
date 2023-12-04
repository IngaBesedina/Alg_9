def binary_search(list_num, first_index, last_index, to_search):
    if last_index >= first_index:
       
        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]
       
 
        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"
 
        elif mid_element > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return binary_search(list_num, first_index, new_position, to_search)
 
        elif mid_element < to_search:
            new_position = mid_index + 1
             # new first index is the new position
            return binary_search(list_num, new_position, last_index, to_search)
 
    else:
        return " Does not appear in the list"
       
list_container = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
search = 34
first = 0
last= len(list_container) - 1
 
print(binary_search(list_container,first,last,search))