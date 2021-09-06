def convertInputString():
    rawInput = input("\nIntroduzca una palabra para saber su es un palindromo: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character)
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "Es un palindromo!" 
    else: 
        return "No es un palindromo." 

def main(): 
    print("\nChecador de palindromo") 
    originalList = convertInputString()  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main() 