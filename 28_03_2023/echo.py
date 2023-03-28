# 'repetitions' represents the number of letters in the first line of echo
# this function prints echoed letters in multiple lines
def echo(text:str, repetitions:int = 4)-> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    """The echoed text starts from the 'repetitions' value till last letter"""
    for i in range(repetitions,0,-1):
        echoed_text = echoed_text + f"{text[-i:]}\n"
    """aggregating the echoed text in multiple lines"""
    return f"{echoed_text.lower()}"

if __name__=='__main__':
    text = input("start yelling...").lstrip()
    print(echo(text))
