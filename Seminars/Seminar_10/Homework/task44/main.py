# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


data_onehot = pd.DataFrame({'human': [True if i == 'human' else False for i in lst],
                            'robot': [True if j == 'robot' else False for j in lst]})
print(pd.get_dummies(lst))
print(data_onehot)



