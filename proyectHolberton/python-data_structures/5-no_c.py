#!/usr/bin/env python3
def no_c(my_string):
    newString =''
    for item in my_string:
        if item !='c' and item !='C':
            newString += item
    return newString    
     