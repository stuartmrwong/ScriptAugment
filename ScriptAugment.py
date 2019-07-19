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
    Sex = {} #define a empty dictionary as Sex
    with open(Editfile) as Oc: #open the new file
        for count, line in enumerate(Oc): #for loop that iterates through each
            #print("Line {}: {}".format(count, line)) #print all the code with line numbers
            Sex.setdefault(count, line) #add each line as key and code as value to the empty dictionary Sex
    #print(Sex) #print Sex just so I can see that it works
    #print(Sex[1]) #proving I can call specific key value pairs
    
    for i in range(1, quarter): #printing the first block
        print(Sex[i])
        
        if '#' in Sex[i] == True:
            #function to replace comments here
            pass
        else:
            pass
    print('END OF BLOCK 1')
    
    
    """
    for i in range(quarter, half): #printing the second block
        print(Sex[i])
    """
    
    
    
        
        
else:
    print('That file doesn\'t exist dumbass') #if file 'a' does not exist, user = dumbass
    

