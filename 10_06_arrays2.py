matrix = [ 
    [1,2,3,4,5], 
    [4,5,6,7,8], 
    [9,10,11,12,13], 
    [14,15,16,17,18], 
    [19,20,21,22,23] 
]

print ("диагональ сверху слева")
for i in range(5):
    print("Индекс i=" + str(i) + " элемент matrix[" + str(i) + "][" + str(i) + "] равен " + str(matrix[i][i]))

    print("\n")



print ("диагональ снизу справа")
for i in range(4, -1, -1):
    print("Индекс i=" + str(i) + " элемент matrix[" + str(i) + "][" + str(i) + "] равен " + str(matrix[i][i]))

    print("\n")



print ("to-do: диагональ сверху справа" )


    





