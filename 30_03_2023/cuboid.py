
x,y,z,n=1,1,2,3


list = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                list.append([i, j, k])
print(list)

## or
##using list comprehension
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n])