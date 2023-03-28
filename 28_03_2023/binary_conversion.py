'''This function is used to convert binary numbers to decimal
Given binary number = (1101)2
Now, multiplying each digit from MSB to LSB with reducing the power of the base number 2.
1 × 2^3 + 1 × 2^2 + 0 × 2^1 + 1 × 2^0
= 8 + 4 + 0 + 1
= 13
'''
def binary_to_decimal(number:str)-> int:
    result = 0
    length_of_binary = len(number)
    for i in number:
        result = result + int(i)*pow(2,length_of_binary-1)
        length_of_binary = length_of_binary-1
    return result


'''To convert binary into octal or hexadecimal
first you need to convert it into decimal then
by reversed concatenation of the remainders you get
the number in the desired base format'''

def binary_convert(binary:str,base:str)-> str:
    result = ''
    #equivalent hexadecimal letters for decimal numbers 
    hex_eq_letters = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    decimal_eq = binary_to_decimal(binary)
    # this block converts input binary number into octal format
    if (base == 'o'):
        #if corresponding decimal number is less than 8 then return the input
        if (decimal_eq<8):
            return decimal_eq
        while(True):
            #if the remainder is 0 then break the loop
            if decimal_eq==0:
                break
            result = result + str(decimal_eq % 8)
            decimal_eq = decimal_eq//8
        # reversing the combined remainder to get octal value
        return result[::-1]
    # this block converts input binary number into hexadecimal format
    elif (base == 'x'):
        if (decimal_eq<10):
            return decimal_eq
        while(True):
            if decimal_eq==0:
                break
            hex_mod = decimal_eq % 16
            # if the corresponding decimal number is between 10 & 15 then get the hexa letter
            if hex_mod in hex_eq_letters:
                hex_mod = hex_eq_letters.get(hex_mod)
            result = result + str(hex_mod)
            decimal_eq = decimal_eq//16
        return result[::-1]
    # this block converts input binary number into binary format
    elif (base == 'b'):
        #removing the leading zeros in the input number
        return binary.lstrip('0')
    # this block converts input binary number into decimal format
    elif (base == 'd'):
        return str(decimal_eq)
    else:
        return binary


'''if you want to convert the input into decimal then input 'd' as base,
    for octal input 'o', for hexadecimal input 'x', for binary input 'b'
    and if you leave input of base empty then it would return the same number
    as input
    '''   
if __name__=='__main__':
    binary = input('Enter the binary number: ').lstrip()
    base = input('Enter the base:').lstrip().lower()
    # get the corresponding base name of the input
    base_dict = {'b':'binary','d':'decimal','o':'octal','x':'hexadecimal'}
    result = binary_convert(binary,base)
    print(f"The converted number in base {base_dict.get(base,None)} is {result}")

  