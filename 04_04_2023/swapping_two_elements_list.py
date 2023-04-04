#swapping function
def swapPositions(list, pos1, pos2):
    val1 = list.pop(pos1)
    #Now the list has been reduced to 3 elements
    val2 = list.pop(pos2-1)
    list.insert(pos1,val2)
    list.insert(pos2,val1)
    
    return list

if __name__=='__main__':
    print(swapPositions([23, 65, 19, 90],0,2))

# list = [23, 65, 19, 90]
# list[1],list[3] = list[3], list[1]
# print(list)
a = 4
b = 3
print(a if a>b else b)
max = lambda a,b: a if a>b else b
print(max(a,b))