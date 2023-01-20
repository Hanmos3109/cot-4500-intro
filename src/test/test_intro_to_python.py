
def printMatrix(matrix):
    for a in Newarray:
        print(" ".join(str(b)for b in a))
    print()


Newarray=[[0]*3 for _ in range(3)]


#Identity matrix
for i in range(len(Newarray)):
    Newarray[i][i] = 1
printMatrix(Newarray)

#Replace 0 with 3
for i in range(len(Newarray)):
    for j in range(len(Newarray[i])):
        if i == j:
            Newarray[i][j] = 1
        else:
            Newarray[i][j] = 3
    #Newarray[i][i] = 1
printMatrix(Newarray)

for a in Newarray:
    a.pop()
printMatrix(Newarray)



