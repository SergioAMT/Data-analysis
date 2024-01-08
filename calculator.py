import numpy as np


def calculate(list):
    ls = np.array(list)
    if len(ls) > 9:
        print("List must contain nine numbers.") 

    mean_rows = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]
    mean_columns = [ls[[0, 3, 6]].mean(), ls[[1, 4, 7]].mean(), ls[[2, 5, 8]].mean()]

    # print ("mean": [mean_columns, mean_rows, ls.mean()])

lista = [2,4,6,8,10]
ls = np.array(lista)
x1 = ls[[0,1,2]].mean()  #los dobles [] son para indices multiples
print(x1)