#pip3 install pikepdf tqdm
import pikepdf
from tqdm import tqdm

print ("---------PDF bruteForce by Emre ISLEK--------")
print ("Put the py file, the wordlist file and the pdf file  you want") 
print ("to crack the password for in  the same folder. Change the name of the pdf file to locked. ")
print ("Change the name of your wordlist file to wordlist. You can work with large files like rockyou or create your own wordlist.")

passwords = [ line.strip() for line in open("wordlist.txt") ]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF
        with pikepdf.open("locked.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the script loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, continue in the script loop
        continue
