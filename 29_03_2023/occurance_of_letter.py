def checkString(input : str)->bool:
    first_letter = input[0]
    if first_letter == 'b' and 'a' in input:
        return False
    for i in range(len(input)):
        '''if the first letter i.e. 'a' matches with the i'th character
          then continue to the next character,if it doesn't match and
           if there's any 'a' in the next characters then return false ''' 
        if first_letter == input[i]:
            continue
        elif first_letter in input[i+1:]:   
            return False
    return True

print(checkString('bb'))


