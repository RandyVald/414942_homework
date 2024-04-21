import pandas as pd
import random

def get_one_hot(data):
    name_col = data.columns[0] 
    set_1 = set()
    list_1 = list()
   
    for name, values in data.iterrows():
        current_value = values[name_col]
        set_1.add(current_value)
        list_1.append(current_value)

    set_1 = sorted(set_1)

    for i in set_1:
        list_next = list() 
        for j in list_1:
            res = i == j
            list_next.append(res)
        data[i] = list_next
    data.drop(name_col,axis=1,inplace=True)    

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print('Исходные данные:')
print(data)
data_test_of_get_dumnies = pd.get_dummies(data['whoAmI'])

print('Данные в виде one hot:')
get_one_hot(data)
print(data)

# Проверка результата
print(data.equals(data_test_of_get_dumnies))

