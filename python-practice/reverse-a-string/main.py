"""
Problem: Reverse A String
"""
from itertools import count
from xml.etree.ElementTree import tostring


def solve():
    pass


# store string to array
# reverse array
# return array

def reverse_string(inputText: str):
    tempArray = []
    resultArray = []
    for c in inputText:
        tempArray.append(c)

    for i in range(len(tempArray) - 1, -1, -1):
        resultArray.append(tempArray[i])
    return ''.join(resultArray)


if __name__ == "__main__":
    print(reverse_string('this is backwards'))
