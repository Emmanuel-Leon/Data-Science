A =[ [2,1,3],[-1,0,2]]
B =[ [-1,0],[-3,3],[2,5]]

filas = len(B)
columnas = len(A)

mult=[]

for i in range(filas):
	for j in range(columnas):
		mult[j][i]=A[j][i]*B[j][i]

print (mult)
