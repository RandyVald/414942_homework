import pandas as pd
import random
# import seaborn as sns
# import matplotlib.pyplot as plt


# print('hello')


lst = ['robot'] * 10
# print(lst)
lst += ['human'] * 10
# print(lst)
random.shuffle(lst)
# print(lst)
data = pd.DataFrame({'whoAmI':lst})

# list_robot = list()
set_u = set()
for i in lst:
    set_u.add(i)

# print(set_u)  
for i in set_u:
    list_next = list() 
    for j in lst:
        res = i ==j
        list_next.append(res)
    data[i] = list_next
    print(list_next)    
# print(list_robot)

# data['robot'] = 

print(data)

# print(data.head(10))
# print(pd.get_dummies(data['whoAmI']))

