def swapList(list):
    length = len(list)-1
    temp = list[0]
    list[0] = list[length]
    list[length] = temp
    return list

if __name__=='__main__':
    li = [12, 35, 9, 56, 24]
    print(swapList(li))
