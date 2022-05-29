import subprocess
with open('tokens.txt', 'r') as tokens, open('wallets.txt', 'r') as wallets:
    lines_t = tokens.readlines()
    lines_w = wallets.readlines()
    for i in range(0,len(lines_t)):
        list_files = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "--allow-unfunded-recipient", lines_t[i].strip(), "1", lines_w[i].strip()], ) # not sure what to do with token ammount: is it the number of tokens? str(len(lines_t))
        list_files.wait()
        print(f"{lines_t[i].strip()} {lines_w[i].strip()}") # you can check if it works here