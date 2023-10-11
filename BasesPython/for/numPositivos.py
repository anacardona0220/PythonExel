# solo los numero positivos

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for item in my_list:
    if item > 0:
      new_list.append(item)
 


print(new_list)