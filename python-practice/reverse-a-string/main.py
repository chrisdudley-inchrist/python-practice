"""
Problem: Reverse A String
"""
from itertools import count


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

    for i in range(len(tempArray),-1,-1,-1):
        print(i)
        resultArray.append(i)
    pass


if __name__ == "__main__":
    reverse_string('this is backwards')
