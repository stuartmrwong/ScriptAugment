# ScriptAugment
The user inputs a path to a python file. ScriptAugment outputs a new file that runs exactly the same as the original input file but any sense of authorship is destroyed.

Given a input path to a .py file:

0. Ensure the output file executes exactly the same as the input file
1. Change the total number of lines
2. Change all comments
3. Change all variables
4. Create meaningless for and while loops
5. Create meaningless try and except clauses
6. Change all imports to import as 
7. Replace similar objects

The output file should be:

0. Work completely as the input code intended
0. Complete obfuscation of authorship
1. Extremely difficult to understand 
2. Comlpetely obvious that an attempt was made to non-surreptitiously obfuscate authorship
