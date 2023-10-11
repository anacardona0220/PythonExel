#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (f"copy {my_list.copy()}")
    else:
        newList = my_list.copy()
        newList[idx] = element
        return newList