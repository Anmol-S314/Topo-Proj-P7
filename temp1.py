import numpy as np

filename = "marschner_lobb_41x41x41_uint8.raw.txt"

dim_x, dim_y, dim_z = 41,41,41
v=dim_x*dim_y*dim_z
a=0
e=0
A = np.fromfile(filename, dtype='uint8', sep="")
A = A.reshape((dim_x, dim_y, dim_z))
c=int(input("Enter the c value: "))

for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]<=c):
                a+=1
                if(i+1 < dim_x):
                    if(A[i+1][j][k]<=c):
                        e+=1
                    
                if(j+1 < dim_y):
                    if(A[i][j+1][k]<=c):
                        e+=1
                        
                if(k+1<dim_z):
                    if(A[i][j][k+1]<=c):
                        e+=1
                        


t=0
k=0
arr=[ [0] * int(e) for i in range(int(v))]

for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]<=c):
                if(i+1 < dim_x):
                    if(A[i+1][j][k]<=c):
                        x=i+j*dim_x+k*dim_x*dim_y
                        y=(i+1)+j*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
 
                if(j+1 < dim_y):
                    if(A[i][j+1][k]<=c):
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j+1)*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1

                if(k+1<dim_z):
                    if(A[i][j][k+1]<=c):
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j)*dim_x+(k+1)*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1

print("Vertices: "+ str(a))
print("Edges: "+ str(e))
rank=np.linalg.matrix_rank(arr)
print("Rank: " + str(rank))
betti_0 = a - rank

print("==========")
print('| \N{GREEK SMALL LETTER BETA}\N{SUBSCRIPT ZERO} =',betti_0,'|')
print("==========")















