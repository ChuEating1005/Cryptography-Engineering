# conda install requests

# 1st: ef0ebbb77298e1fbd81f756a4efc35b977c93dae -> orange
# 2nd: 0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2 -> starfish
# 3rd: 9d6b628c1f81b4795c0266c0f12123c1e09a7ad3 -> rebull + puppy

import hashlib, requests, time

url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"

hash_check = input('Hash: ')
data = requests.get(url).text.split('\n')

clock = time.time()
for attempt, password in enumerate(data):
    hash_code = hashlib.sha1((password).encode()) # change password to 'redbull' + password for 3rd problem
    if (hash_code.hexdigest() == hash_check):
        clock = time.time() - clock
        print(f"The password is: {password}")
        print(f"Took {attempt} attempts to crack input hash. Time Taken: {clock} seconds")
        break
