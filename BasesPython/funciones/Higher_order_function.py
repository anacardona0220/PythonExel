# function tradicional 

# def increment(a):
#  return a * 2

# print(increment(3))
# print('')
# # ----- Version lambda ----------

increment_v2 =  lambda a : a * 4

 

high_ord_func = lambda x, func: x + func(x)
result = high_ord_func(2, increment_v2)
print(result) 

result_v2 = high_ord_func(2, lambda a : a * 4)
print(result_v2)