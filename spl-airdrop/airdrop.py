import subprocess
from security import safe_command

with open('airdrop.txt', 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    for i, line in enumerate(lines):
        list_files = safe_command.run(subprocess.Popen, ["spl-token", "transfer", "--fund-recipient", "--allow-unfunded-recipient", "TOKEN_ADDRESS", "TOKEN_AMOUNT",lines[i].strip()], )
        list_files.wait()
    f.seek(0)
    for line in lines:

        f.write(line)
        print(line)
