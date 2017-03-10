import os
import random
import time

target = "I love you."

current = ""

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!?/[]{}();':1234567890"

def getRandomLetter(currentString):
    return currentString + random.choice(alphabet)

for letter in target:
    current = getRandomLetter(current)

while current != target:
    os.system("cls")
    newString = ""
    for index in range(len(target)):
        if current[index] == target[index]:
            newString += current[index]
        else:
            newString = getRandomLetter(newString)
    current = newString
    print(current)

    time.sleep(0.01)
    