"""
Pig Latin – Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an
English word the initial consonant sound is transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
"""

userWord = input("Enter word to convert to Pig Latin: ")
vowels = ['A', 'a', 'I', 'i', 'E', 'e', 'O', 'o', 'U', 'u', 'Y','y']

i = 0


while(i<len(userWord)):
    if(userWord[i] in vowels):
        print(userWord+"ay")
        break
    elif(i==len(userWord)-1):
        userWord = userWord[1:] + userWord[0]
        print(userWord)
    else:
        userWord = userWord[1:]+userWord[0]
