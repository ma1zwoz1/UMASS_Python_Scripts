# -*- coding: utf-8 -*-
"""
@author: Zachary Wozich
Assignment 2
Class - Info 2820

Program: phone numbers
For this assignment you will be creating a Python script to lookup phone numbers in a data file given a user-provided last name, or a first and last name.
The script should look up all entries in the data file that match the user’s request and display them to the screen in the following format (notice that the format includes a comma appended to the last name.)
<first name> <last name>, <phone number>
For example, the following are test runs of the program with expected output.
Enter a last name, or first and last name: smith
Drew Smith, 412-555-2121
Elizabeth Smith, 412-555-2121
Enter a last name, or first and last name: drew smith
Drew Smith, 412-555-2121
Data file – phones.txt
The program should use the file phones.txt as the data file containing the list of known names and numbers. phones.txt has the following format, where the first column is the first name, the second column is the last name, and the last column is the phone number.
Pradeep Acharya 301-555-3276
John Brady 321-555-6932
James Chen 256-555-3331
Josh Kelly 424-555-4053
Brady Parker 756-555-3828
Drew Smith 412-555-2121
Elizabeth Smith 412-555-2121
To download phones.txt from within Blackboard, right-click on the file and select “Save link as…” Make sure to save the file to the same folder you plan to write your script in so it will be found when you use the open function to open it (otherwise, you will have to provide a full pathname for the file to the open function.)
Requirements:
1. Name your script <your-last-name>_phones.py
2. The input:
a. Use the input function and have one prompt that asks the user to enter a last name, or a first and last name (separated by whitespace).
It should print an error if no names are given or more than two are given. b. The program should work if the user enters names in uppercase, lowercase, or a mix of case. Since the names in the file phones.txt are of mixed case, for comparisons, you’ll want to make use of the string method .lower() to convert both the input strings and those read from the file to lowercase.
c. Use the string .split() method on the input to split it into a list of strings, then assign the input to string variables first_name and last_name based on whether the length of the string is one element or two. Also convert the strings to lower case using .lower().
3. Open phones.txt and loop through each line in the file to see if it matches the provided input. When a match is found, display the output in the following format:
<first name> <last name>, <phone number>
4. Follow all previously discussed guidelines including proper variable naming, code documentation, and inclusion of a docstring header that includes a description of the program, your name and the date.
Test cases:
When you’re done writing your program you should test it using the input from these examples so you know your program is functioning correctly.
Enter a last name, or first and last name: smith
Drew Smith, 412-555-2121
Elizabeth Smith, 412-555-2121
Enter a last name, or first and last name: drew smith
Drew Smith, 412-555-2121
Enter a last name, or first and last name: brady
John Brady, 321-555-6932
Enter a last name, or first and last name: parker
Brady Parker, 756-555-3828
"""

#Create empty list
phones_names=[]

#open phone text file
phoneFile = open("phones.txt", 'r')

#for loop to break up first and last name into 1 list and phone number into another list

for phone_name in phoneFile:
    temp = phone_name[:len(phone_name) - 13] #extract first and last name
    #append both list together seperated by comma
    phones_names.append(temp + "," + " " + phone_name[-13:]) # extract phone number
    
#take user input to lower
phonenumber = input("Enter a last name, or first and last name: ").lower()

#input counter        
input_count = len(phonenumber.split())

#input word count logic   
if (input_count != 0 and input_count <= 2):
    
    for line in phones_names: #iterate thought list
        if phonenumber in line.lower(): #compare input to list entries
            print(line) # print line in list that match
            
#print error upon bad input            
else:
    print("invaid input, Enter a last name, or first and last name:")
        

    
    



    

  
    
