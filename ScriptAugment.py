# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:22:28 2019

@author: Stuart
"""

"""
given user input of a file,
read the file and write with the intent to obscure authorship
"""

import os
import shutil
import re
import random
import string
from collections import OrderedDict

def remove_comment(line, finish):
    line = line[0: finish] #remove the comment by slicing the string with the index of the start to the #
    return line
                  
def add_comment():
    line = str('#')
    return line

def create_noise(length, chars):
    return '#' + ''.join(random.choices(chars, k=length)) + '\n'
        
def add_remove_line(line):
    d20 = random.randint(1,20) #random integer between 1 and 20, not crypto secure
    if d20 <= 2: #20% chance to add a line
        line = line + '\n'
    if d20 >=19: #20% chance to strip the line
        line = line.strip()
    else:
        pass
    return line
    
def file_length(filename): #this function will calculate the number of lines
    with open(filename) as f: #open the file and call it f
        for i, l in enumerate(f): #start a for loop that counts each line
            pass #do nothing
    return i + 1 #the function returns the number of lines + 1 because 0 counts

"""
    the function to replace comments goes here
"""

print('name of file, including directory') #ask user for the file to edit
Truefile = input() #save the file as variable 'a'

if os.path.exists(Truefile): #check that the file 'a' actually exists
    Editfile = shutil.copyfile(Truefile, str(Truefile[0:-3]) + 'edit.py') #create a copy and name it 'file'+'edit'
    
    #as of here we can stop touching the Truefile
    
    Totallines = file_length(Editfile)
    print('this file is ' + str(Totallines) + ' lines long')
    
    c = open(Editfile,'r')#open the new file in read only mode
    Oldcode = c.read()
    #print('This is the old code: \n\n\n' + Oldcode)
    c.close()
    Newcode = '' #this will hold our new, obfuscated code
    
    quarter = Totallines / 4
    quarter = int(quarter)
    half = quarter * 2
    half = int(half)
    threequarter = quarter * 3
    threequarter = int(threequarter)
    
    print('We will divide the program into 4 parts.')
    print('Part 1 will be line 1 - ' + str(quarter))
    print('Part 2 will be line ' + str(quarter) + ' - ' + str(half))
    print('Part 3 will be line ' + str(half) + ' - ' + str(threequarter))
    print('Part 4 will be line ' + str(threequarter) + ' - ' + str(Totallines))
    print('\n')
    
    """ this prints each line with a line number"""
    CodeDict = {} #define a empty dictionary as CodeDict
    with open(Editfile) as Oc: #open the new file
        for count, line in enumerate(Oc): #for loop that iterates through each
            #print("Line {}: {}".format(count, line)) #print all the code with line numbers
            CodeDict.setdefault(count, line) #add each line as key and code as value to the empty dictionary CodeDict
    #print(CodeDict) #print CodeDict just so I can see that it works
    #print(CodeDict[1]) #proving I can call specific key value pairs
    
    #START BLOCK 1
    #scanning through the first block(25% of the code)
    for i in range(0, threequarter): 
        
        #if you find a shebang, dont do anything 
        if CodeDict[i].find('#!') >= 0: 
            print('Shebang found')
            Newcode += CodeDict.get(i)
            pass           
        
        #if we find a comment, delete the comment, write a new comment
        elif CodeDict[i].find('#') >= 0: 
            CommentLocation = CodeDict[i].find('#')                    #acquire the location of the #                    
            print('Comment Detected in line ' + str(i) + ' at character ' + str(CommentLocation))
            CodeDict[i] = remove_comment(CodeDict[i], CommentLocation) #slice out the comment and leave anything else
            print('Creating new line: ' + str(CodeDict.get(i)))        #get the new, sliced line                  
            Newcode += CodeDict.get(i) + str(create_noise(30, string.ascii_letters + string.digits + string.punctuation))            #add a comment back in because there was one before
        
        #if we find an empty line, randomly add another or delete it
        elif '\n' in CodeDict[i] == True:
            print('\n>>>new line detected. calculating to add or delete')
            CodeDict[i] = add_remove_line(CodeDict[i])
            print(CodeDict[i])
            
        #if its something we dont recognize, leave it to ensure functionality
        else:
            print(CodeDict[i])
            Newcode += CodeDict.get(i)
            pass
            
    print('END OF BLOCK 1')
    print('New code: ')
    print(Newcode)
    #END OF BLOCK 1
    """
    #scanning through the second block(25% - 50% of the code)
    for i in range(quarter, half): 
               
        #if we find a comment, delete the comment, write a new comment
        if CodeDict[i].find('#') >= 0: 
            CommentLocation = CodeDict[i].find('#')                    #acquire the location of the #                    
            print('Comment Detected in line ' + str(i) + ' at character ' + str(CommentLocation))
            CodeDict[i] = remove_comment(CodeDict[i], CommentLocation) #slice out the comment and leave anything else
            print('Creating new line: ' + str(CodeDict.get(i)))        #get the new, sliced line                  
            Newcode += CodeDict.get(i) + str(create_noise(30, string.ascii_letters + string.digits + string.punctuation))            #add a comment back in because there was one before
            
        elif '\n' in CodeDict[i] == True:
            print('\n>>>new line detected. calculating to add or delete')
            CodeDict[i] = add_remove_line(CodeDict[i])
            print(CodeDict[i])
        
        else:
            print(CodeDict[i])
            pass
            
    print('END OF BLOCK 2')
    print('New code: ')
    print(Newcode)
    #END OF BLOCK 2
    """
    with open(Editfile, 'w') as Nc:
        Nc.write(Newcode)
        
    
    """
    for i in range(quarter, half): #printing the second block
        print(CodeDict[i])
    """
    
    
    
        
        
else:
    print('That file doesn\'t exist dumbass') #if file 'a' does not exist, user = dumbass
    

