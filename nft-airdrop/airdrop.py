import os  #send commands to terminal/cmd
import csv  #for csv/spreadsheet manipulation
import datetime  #I wanted to time stamp the output file
import secrets

with open("token.txt", "r+") as t:  #open the file containing token addresses as read/write and store it as variable "t"
    lines = t.readlines()  #read the lines from the token file and store the addresses as <a list?> in variable "lines"
    token = []  #create an empty list called "token"
    for i in lines:  #for each item "i" in <list?> "lines" do the following
        i = i.strip()  #strip whitespace and escape characters from item "i"
        token.append(i)  #append item "i" to list "token"
        tokenCount = len(token)  #save the number of items in list "token" to variable "tokenCount"

with open('airdrop.txt', 'r+') as f: #open the file containing receiving addresses as read/write and store it as variable "f"
    lines = f.readlines()  #read the lines from the addresses file and store the addresses as <a list?> in variable "lines"
    address = []  #create an empty list called "address"
    for i in lines:  #for each item "i" in <list?> "lines" do the following
        i = i.strip()  #strip whitespace and escape characters from item "i"
        address.append(i)  #append item "i" to list "address"
        addressCount = len(address)  #save the number of items in list "address" to variable "addressCount"

secrets.SystemRandom().shuffle(token)  #rearrange the items of list "token"
secrets.SystemRandom().shuffle(address)  #rearrange the items of list "address"

if addressCount > tokenCount:  #check if the vairable "addressCount" is larger than "tokenCount" and makes sure every token gets matched to an address with addresses left over
    count = tokenCount - 1  #counting for loops starts at 0 not 1, this fixes an error
else:  #if "addressCount" is smaller than "tokenCount" each address will get a token with tokens left over
    count = addressCount - 1  #counting for loops starts at 0 not 1, this fixes an error

def Send(token, address):  #defines the function "Send", which requires the lists stored as variables "token", and "address"
         command =  'spl-token transfer --fund-recipient --allow-unfunded-recipient '+ token[c] + " 1  " + address[c]  #this is the command to be sent to terminal/cmd; "token[c]" and "address[c]" will change with each iteration of the following loop
         os.system(command)  #sends the "command" variable to the terminal for execution

with open('dropResult.csv', 'w') as w:  #creates/opens the file "dropResult.csv" in write mode and stores it in variable "w"
    w.truncate()  #empties the "dropResult" file
    w.close()  #closes the "dropResult" file

c = 0  #creates and sets the variable "c" to 0
while c <= count: #the conditions for the loop are: as long as "c" is less than or equal to the shortest list of "token" or "address" as counted in lines 12 &2 0 it will do the following
    Send(token, address)  #Calling the function defined at line 30
    print(str(c) + " of " + str(count))  #displaying which iteration of the loop we are on
    now = datetime.datetime.now()  #getting the date and time
    now = now.strftime("%Y-%m-%d %H:%M:%S")  #formatting the date and time
    line = address[c] + "," + token[c] + ',' + now  #storing which address received which token at the time it was sent

    with open('dropResult.csv', 'a', newline='\n') as w:  #opens the file "dropResult.csv" in append mode and stores it in variable "w"
        w.write(line + '\n')  #writes the information defined in variable "line" (44) to the file
    c += 1  #increase variable "c" by 1

print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")  #a final message for the user
input("Press Enter(Return) to close")  #holds the program open so the user may see the results and final message
