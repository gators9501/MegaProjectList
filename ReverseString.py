# Accept string from user and print the reverse

userInput = input("Enter a string: ")

reverseString = ""

reverseIndex = 0
inputLength=len(userInput)

loopCounter = 0

while loopCounter<inputLength:
    reverseString = userInput[loopCounter] + reverseString
    loopCounter+=1

print(reverseString)



