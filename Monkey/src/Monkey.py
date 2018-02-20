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

def Score(phrase,actual):
    score = 0
    for k in range(len(actual)):
        if phrase[k] == actual[k]:
            score = score + 1
    
    return score / len(actual)

def Improve(phrase,actual):
    pool = "abcdefghijklmnopqrstuvwxyz "
    sentence = list(phrase)
    for k in range(len(actual)):
        if sentence[k] != actual[k]:
            sentence[k] = pool[random.randrange(len(pool))]
            newsentence = ''.join(sentence)
            return newsentence
        else:
            return phrase
def main():
    statement = "methinks it is like a weasel"
    current_score=0
    
    newstring = Gen(28)
    newscore = Score(newstring,statement)
    while newscore < 1:
        if newscore > current_score:
            print(newstring + " score is " + str(newscore))
            current_score = newscore
        newstring = Improve(newstring,statement)
        newscore = Score(newstring,statement)
main()
# pool = "abcdefghijklmnopqrstuvwxyz "
# print (pool)