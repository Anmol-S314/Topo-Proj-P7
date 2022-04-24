import sympy as sym
import numpy as np
import scipy.linalg.interpolative as sli
import time
from ast import Break
import numpy as np
from PIL import Image
import rawpy


begin=time.time()

t=30
precis=20
count=0
LENGTH,BREADTH,HEIGHT=(41,41,41)
bruh=[]
vis=[]
edgey=[]
#bruh = [[[[0]*LENGTH]*BREADTH]*HEIGHT]
for i in range(LENGTH):
  bruh.append([])
  vis.append([])
  for j in range(BREADTH):
    bruh[i].append([])
    vis[i].append([])
    for k in range(HEIGHT):
      bruh[i][j].append(0)
      vis[i][j].append(0)
fin=open('nucleon.raw')
#print(fin)


img=np.fromfile(fin,dtype=np.uint8,count=LENGTH*BREADTH*HEIGHT)
print("Dimension of the old image array: ", img.ndim)
print("Size of the old image array: ", img.size)
for i in range(LENGTH):
  for j in range(LENGTH):
    for k in range(LENGTH):
      if(img[LENGTH*LENGTH*i + LENGTH*j + k]<=t):
        bruh[i][j][k]=img [LENGTH*LENGTH*i + LENGTH*j + k]
      else:
        bruh[i][j][k]=0

def addEdge(a,b):
    edgey.append([a,b])

for i in range(41-precis):
  for j in range(41-precis):
    for k in range(41-precis):
        if(bruh[i][j][k] > 0):
            count=count + 1
            if(bruh[i][j][k+3]!=0):
                addEdge(LENGTH*LENGTH*i + LENGTH*j + k, LENGTH*LENGTH*i + LENGTH*j+ k + precis)
            elif(bruh[i][j+3][k]!=0):
                addEdge(LENGTH*LENGTH*i + LENGTH*j + k, LENGTH*LENGTH*i + LENGTH*(j+precis)+ k)
            elif(bruh[i+3][j][k]!=0):
                addEdge(LENGTH*LENGTH*i + LENGTH*j + k, LENGTH*LENGTH*(i+precis) + LENGTH*j+ k)


fin.close()
stro = str(count)
stre = str(len(edgey))
f = open("out.gts","w")
f.write(stro+ " "  + stre + " " + "0")
f.write("\n")
for i in range(41):
  for j in range(41):
    for k in range(41):
        if(bruh[i][j][k]!=0):
            f.write(str(i)+ " " +str(j)+ " "+ str(k))
            f.write("\n")
for i in range(len(edgey)):
    f.write(str(edgey[i][0])+ " " + str(edgey[i][1]))
    f.write("\n")
f.close()




