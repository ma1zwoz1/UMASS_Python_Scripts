# -*- coding: utf-8 -*-
"""
@author: Zachary Wozich
Assignment 3
Class - Info 2820

Program: phone numbers
The program will the user if they’d like to lookup up phone numbers or addresses. 
The program should repeatedly ask the user for a person’s name (first and last name) and look up and display the appropriate information. 
Error conditions are  handled appropriately.
The user should see the following output:

Lookup (1) phone numbers or (2) addresses: 2
Enter space-separated first and last name: Buck Rogers
error: person not found.
Enter space-separated first and last name: Drew Smith
Street: 285 Andover Lane
City: Pompano Beach
State: FL
Zip Code: 33060
Enter space-separated first and last name: Josh Kelly
Street: 7416 Monroe Ave.
City: Media
State: PA
Zip Code: 19063
Enter space-separated first and last name:    


"""
#main function
def main_menu():
    # This initiates the address books and allows users to select which feature to use      
#    while True:
#        try:
    selection = int(input("Lookup (1) phone numbers or (2) addresses: ")) #enter selection
#        except ValueError:
#            print("This is not a whole number.")
#        continue
    while True: #enter while loop
            if (selection == 1): #selection for phone numbers
                 names = input("Enter space-separated first and last name: ").lower() #enter name to lower case
                 input_count = len(names.split()) # split name to count number of words
                 if (input_count != 0 and input_count <= 2): #if to enter if number of words are correct
                         found = False
                         for name in dict: #iterate though list
                             if names in dict[name]['name'].lower():  #find dict name and set to lower
                                 dict_pop = dict[name].pop('phone') #pop out phone number
                                 print ("phone:",      dict_pop) #print phone number
                                 found = True
                                 break
                             elif not found:
                                print("error: person not found.") #not found print error
                                continue
                 elif input_count == 0: #break out if word input count = zero
                    break
                 else:
                    print("ERROR Please enter a valid first and last name") #break out if word input count is more than 2 words
                    break
            elif (selection == 2):
                 names = input("Enter space-separated first and last name: ").lower()
                 input_count = len(names.split())
                 if (input_count != 0 and input_count <= 2): #if to enter if number of words are correct
                         found = False
                         for name in dict: #iterate though list
                             if names in dict[name]['name'].lower(): #find dict name and set to lower
                                 for sub_nest in dict[name]:
                                    print (sub_nest, ':'  , dict[name][sub_nest]) #print address
                                 found = True
                                 break
                             elif not found:
                                print("error: person not found.") #not found print error
                                continue
                 elif input_count == 0: #break out if word input count = zero
                    break
                 else:
                    print("ERROR Please enter a valid first and last name") #break out if word input count is more than 2 words
                    break
                    
dict= {} #dictionary

def get_addresses_func():   
#function to load text into dictionary
    try:
        with open("address.txt","r") as read: #read in text file
            for line in read:
                (name, address, city, state, zipcode, phone ) = line.split(',') #break out values by commma
                dict.update({name : {'name': name, 'address' : address, 'city' : city, 'state' : state, 'zip' : zipcode, 'phone': phone }}) #write values to dictionary
    except IOError: #if io error exit from import
        exit()
    
    print ("This dictionary contains these keys: ", " , ".join(dict)) # print dictionary keys
    
if __name__ == '__main__':
   
    addresses = get_addresses_func() #run get addresses from dictionary
    
    main = main_menu() # run main logic
          
      
 
    
    

        

    
    



    

  
    
