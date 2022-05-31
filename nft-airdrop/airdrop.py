import os
import random
import csv
import datetime

with open("token.txt", "r+") as t:
    lines = t.readlines()
    token = []
    for i in lines:
        i = i.strip()
        token.append(i)
        tokenCount = len(token)

with open('airdrop.txt', 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    address = []
    for i in lines:
        i = i.strip()
        address.append(i)
        addressCount = len(address)

random.shuffle(token)
random.shuffle(address)

if addressCount > tokenCount:
    count = tokenCount - 1
else:
    count = addressCount - 1

#def Send(token, address): 
#         command =  'spl-token transfer --fund-recipient --allow-unfunded-recipient '+ token[c] + " 1  " + address[c]
#         os.system(command)

with open('dropResult.csv', 'w') as w:
    w.truncate()
    w.close()

c = 0
while c <= count:
#    Send(token, address)
    print(str(c) + " of " + str(count))
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    line = token[c] + "," + address[c] + ',' + now

    with open('dropResult.csv', 'a', newline='\n') as w:
        w.write(line + '\n')
    c += 1

print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")
input("Press Enter(Return) to close")
