"""
Count Vowels – Enter a string and the program counts the number of vowels in the text. For added complexity have it
report a sum of each vowel found.
"""

vowelCount = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

userInput = input("Enter string to get vowel count: ").upper()

for c in userInput:
    if c in vowelCount:
        vowelCount[c] = vowelCount[c] + 1

print(vowelCount)