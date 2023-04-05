import math
def countPlateOnTable(n, R, r):
    # write your code here
    ratio = r/(R-r)
    sin = math.sin(math.pi/n)
    if n==1 and R>=r:
        return 'Yes'
    elif n!=1 and R==r:
        return 'No'  
    elif sin>=ratio:
        return 'Yes'
    else:
        return 'No'
print(countPlateOnTable(4, 10, 4))