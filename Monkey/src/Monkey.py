'''
Created on Feb 20, 2018

@author: Eugene Yu
'''

import random

def Gen(n):
    pool = "abcdefghijklmnopqrstuvwxyz "
    sentence = ""
    for k in range(n):
        sentence = sentence + pool[random.randrange(len(pool))]
    return sentence

#the score is not cool
def Score(phrase,actual):
    score = 0
    for k in range(len(actual)):
        if phrase[k] == actual[k]:
            score = score + 1
    
    return score / len(actual)

def Improve(phrase,actual):
    pool = "abcdefghijklmnopqrstuvwxyz "
    sentence = list(phrase)
    counter = 0
    for k in range(len(actual)):
        if sentence[k] != actual[k]:
            counter = counter + 1
    if counter != 0:
        for k in range(len(actual)):
            if sentence[k] != actual[k]:
                randchoice = pool[random.randrange(len(pool))]
                sentence[k] = randchoice
                newsentence = ''.join(sentence)
                return newsentence
    else:
        return phrase

def main():
    statement = "methinks it is like a weasel"
    
    newstring = Gen(28)
    newscore = Score(newstring,statement)
    while newscore < 1:
        currentstring=newstring
        print(currentstring + " score is " + str(newscore))
        newstring = Improve(currentstring,statement)
        newscore = Score(newstring,statement)
    print(newstring)
main()