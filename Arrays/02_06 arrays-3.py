matrix = [ 
    [1,2,3,4,5], 
    [4,5,6,7,8], 
    [9,10,11,12,13], 
    [14,15,16,17,18], 
    [19,20,21,22,23] 
]
for i in range(5):
    if i % 2 != 0:
        for j in range(5):   
            print(matrix[i][j])
    else:
        for j in range(4, -1, -1):
            print(matrix[i][j])

    print("\n")