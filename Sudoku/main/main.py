'''
Created on Feb 19, 2018

@author: Eugene Yu
'''
import random
pool = "abcdefghijklmnopqrstuvwxyz "
phrase = "abcdefghijklmnopqrstuvwxyz  "
statement = "methinks it is like a weasel"

sentence = list(phrase)
for k in range(28):
    if phrase[k] != statement[k]:
        sentence[k] = pool[random.randrange(len(pool))]
        newsentence = ''.join(sentence)
        print(newsentence)
