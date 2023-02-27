import string

# A list containing all characters
all_letters= string.ascii_letters

def encryptMessage(msg,key):
    """
    create a dictionary to store the substitution
    for the given alphabet in the plain text
    based on the key
    """
    # msg= list(msg)
    dict1 = {}
    key=int(key)
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]

    cipher_txt=[]

    # loop to generate ciphertext
    for char in msg:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp =char
            cipher_txt.append(temp)
            
    cipher_txt= "".join(cipher_txt)
    return cipher_txt

	

def decryptMessage(cipher,key):
    # cipher=list(cipher)
    dict2 = {}
    key=int(key)
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
        
    # loop to recover plain text
    decrypt_txt = []

    for char in cipher:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
            
    decrypt_txt = "".join(decrypt_txt)
    return decrypt_txt

# print(encryptMessage("hello","2"))
# msg = input()
 
# cipher = encryptMessage(msg)
# print("Encrypted Message: {}".format(cipher))
 
# print("Decryped Message: {}".format(decryptMessage(cipher)))