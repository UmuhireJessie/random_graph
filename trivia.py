# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 14:12:12 2022

@author: HP
"""

import random
import time


lisQ = [
        '--- refers to a block of code which is used to initialize an object.', 
        'What is JDK? ', 
        '---- convert the Java primitives into the reference types (objects).', 
        'What is JIT ', 
        '---- are special keywords which are used to restrict the access of a class ', 
        'What is used to represent the behavior of an object? ', 
        'When the ---- is used with a variable then its value can’t be changed once assigned '
        ]

lisA = ['constructor', 'Java Development Kit', 'Wrapper classes', 'Just-In-Time', 'access modifiers', 'methods', 'final keyword']



print("""
         ----- WELCOME TO THE GAME ------
         
       INSTRUCTIONS: 1).....
                     2)....
                     3)....
                     4)....""")

while True:
    
    uniqueIndeces = random.sample(range(0,7), 5) 
    
    num = random.choice(uniqueIndeces)
    
    multipleAnswer = [lisA[uniqueIndeces[0]], lisA[uniqueIndeces[1]], lisA[uniqueIndeces[2]], lisA[uniqueIndeces[3]], lisA[uniqueIndeces[4]]]
    
    a = multipleAnswer[0]
    b = multipleAnswer[1]
    c = multipleAnswer[2]
    d = multipleAnswer[3]
    e = multipleAnswer[4]
    
    print(f'\nQuestion:  {lisQ[num]}\n')
    
    print(f'''Choose a letter corresponding to the correct answer:
                  A.{a}
                  B.{b}
                  C.{c}
                  D.{d}
                  E.{e}\n''')
                  
    startime = time.time()
    answerUser = input("Answer:  ").lower().strip()
    runTime = time.time() - startime
    
    try:
        if globals()[answerUser] == lisA[num]:
            print('\nCorrect!')
            print(runTime, 'seconds')
            
        else:
            print('Wrong!')
            print(runTime, 'seconds')
                
    except KeyError:
        print('Wrong!')
        print(runTime, 'seconds')
        
        
    wantPlay = input('Do you want to play?(Y/N) ').lower().strip()
    if wantPlay == 'y': 
        continue
    else: 
        break
