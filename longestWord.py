"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""

import re

def longestWord(text):
    myString = re.findall(r"[A-Za-z']+", text)  # Use rEGEX search entire string and take only alphebetical letters 
    maxList = myString[0] 
    for i in range(1, len(myString)):
        if len(myString[i]) > len(maxList):
            maxList = myString[i]
    return maxList

