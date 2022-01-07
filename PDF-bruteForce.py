#pip3 install pikepdf tqdm

import pikepdf
from tqdm import tqdm

passwords = [ line.strip() for line in open("wordlist.txt") ]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # PDF file
        with pikepdf.open("locked.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue