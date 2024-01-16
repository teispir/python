def remove_repeated_elements(lst):
    # convert list to set
    set_from_list = set(lst)
    
    # convert set back to list
    unique_list = list(set_from_list)
    
    return unique_list

# example usage
lst = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
print(remove_repeated_elements(lst))