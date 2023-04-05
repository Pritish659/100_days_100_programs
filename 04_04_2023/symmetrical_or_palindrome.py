str = 'amaam a'
def check_symmetrical_palindrome(str:str)->str:
    '''checking if a string is palindrome and symmetrical'''
    # replacing any whitespace
    str = str.replace(" ","").lower()
    half = len(str)//2
    if len(str)%2 == 0:
        if str[:half] == str[half:]:
            print('symmetrical')
        else:
            print('not symmetrical')
    else:
        if str[:half] == str[half+1:]:
            print('Symmetrical')
        else:
            print('not symmetrical')
    
    # checking if the string is palindrome or not
    if str == str[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')
    
if __name__ == '__main__':
    check_symmetrical_palindrome(str)

'''Alternate method'''
"""
str = 'amaam a'
str = str.replace(" ","").lower()
length = len(str)
# to calculate middle value accordingly
if length%2 == 0: 
    half = length//2 # for even length
else: 
    half = length//2 + 1 # for odd length
# checking if the string is symmetrical
print(half)
flag = 0
i = 0
j = half
while(i < half and j < length-1):
    if str[i] == str[j]:
        i += 1
        j += 1
    else:
        flag = 1
        break
if flag ==0:
    print(f"The given string {str} is symmetrical")
else:
    print("not")

# To check if the string is palindrome
start = 0
end = len(str) - 1
flag = 0
while(start < end):
    if str[start] == str[end]:
        start += 1
        end -=1
    else:
        flag = 1
        break
if flag ==0:
    print(f"The given string {str} is palindrome")
else:
    print('not')

"""




