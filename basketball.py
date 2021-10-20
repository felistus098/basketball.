# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:18:00 2021

@author: Felistus
"""

import random

shootingArray = ['miss', 'shot'] # array that holds the a miss and a shot
missCount = 0 # count the number of misses
shotCount = 0 # count the number of shots
streakOfMissesCount = 0 # count the number of times he makes 7 or more misses. 
trials = 1000

def shoot():
    global missCount, shotCount, streakOfMissesCount # make the variables to be acceses within the whole program
    
    # the for loop below will simulate 10 throws
    for i in range(1,11):
        goalOption = random.choices(shootingArray, weights=(0.53, 0.47), k=1) # random.choices allows us to give one choice more weight than another choice
# the values in shootingArray will be given custom chances of being chosen(miss will have a 0.53 chance of being chosen)
# k=1 tells the method to return one value 
        
        # depending on the random choice above, either increment missCount or shotCount 
        if goalOption[0] == 'miss':
            missCount += 1
            
        if goalOption[0] == 'shot':
            shotCount += 1
    
    print('Missed shots:',missCount, '...Shots entered:', shotCount)
    print('shots:',shotCount, '...miss entered:', missCount)

    # if number of misses in 10 throws is greater than 7 then increment the streakOfMissesCount    
    if missCount >= 7:
        streakOfMissesCount += 1
        
    print('Number of missing streaks: ',streakOfMissesCount, '*', '\n')
     
    # initialize our miss and shot count to zero 
    missCount = 0 
    shotCount = 0


# simulate the ten throws over a number of times. 
# the probability that he will have 7/10 misses is given by streakOfMissesCount divided by total trials
for i in range(1,trials):
    shoot() 
    prob = streakOfMissesCount / trials
    print('Missing streak probability: ', prob)
    
print('Number of trials : ',trials, '*', '\n')    