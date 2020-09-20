###SHA1 Password Crack

def sha1Crack():
    import hashlib
    import ctypes
    import urllib
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------------SHA1------------------------------------------------------------------------\n")
    print("\nSHA1 is one of the oldest hashing methods, and has sense been made obsolete by other, newer methods.",
          "\nIt was made obsolete due to its likelihood of 'collisions', which are two different inputs creating the same hash value.",
          "\nBesides its collision likelihood, it was also made insecure by improvements in computing speeds being able to hack the hashes to find their original values.",
          "\n\nHowever, it is very simple to see how it works, so it is good to use to conceptualize what a hash is.",
          "\n\nAn SHA1 hash is made by first adding a 'salt' to the plain-text input before hashing.",
          "\nA salt is just a random string of characters added to the beginning or end of the input to increase difficulty in cracking the hash.",
          "\nThen an algorithm is performed on the newly altered input to create our hash.",
          "\n\nAn SHA1 hash is always 40 digits long (160-bit; 20-byte)",
          "\nTry it for yourself now!\n")
          
    password = input("Input a common password to hash: ")
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()

    print("Thanks! Now re-enter the password and we will compare them to see if they are the same!: ")

    second_password = input("Confirm the password: ")
    setpass = bytes(second_password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    confirm_pw = hash_object.hexdigest()

    print("\nHash of first entered password: ", guess_pw)
    print("Hash of second entered password: ", confirm_pw)

    if(guess_pw == confirm_pw):
        print("\nPasswords are the same")
        print("The hash values of the two passwords are the same")
    else:
        print("\nInvalid combination; passwords not the same")
        print("The hash values of the two passwords are NOT the same")


    print("\nGreat! Now that we can see how two passwords are comapared without them being in plain-text, let's try cracking the password!")
    print("\nCopy the hash value of one of the above passwords and paste it below. It's hacking time!")



    sha1hash = input("Please input the hash to crack: ")
    common_passwords = open("common_passwords.txt", encoding='utf-8').read().splitlines()

        
    for guess in common_passwords:
        hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if(hashedGuess == sha1hash):
            print("The password is: ", str(guess))
            print("\nGreat! You hacked the password!",
                  "\nWhat happeneded here was the code took the hashed value and compared it to the hash values of a text file filled with the most common passwords in the world.",
                  "\nIf it found a match, it printed it out here in plaintext!",
                  "\n\nThis can be used practically by intercepting hashed password values and then applying this method to break them\n")
            break

    try:
        hash_mode = int(input("Type 1 to redo this hash type, 2 to go to another hash type, or 3 to exit, and press 'Enter': "))
    except ValueError:
        print("\nThat's not an integer... come on man please, you know what a number is\n")
        first_code()
        
    if(hash_mode == 1):
        sha1Crack()
    elif(hash_mode == 2):
        first_code()
    elif(hash_mode == 3):
        exit
    else:
        print("That wasn't an option, returning to hash types\n")
        first_code()            
    



###SHA256 Password Crack

def sha256Crack():
    import hashlib
    import ctypes
    import urllib
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------------SHA256------------------------------------------------------------------------\n")
    print("\nSHA256 is a modern improvement on SHA1, and is much more secure against hacking attempts.",
          "\nThis security mostly comes from the fact that is it much longer than an SHA1 hash, and therefore takes much more time to make, and computing power to hack.",
          "\nIt is also much more collision-resistent than its predecessor, meaning that it's very unlikely for two different inputs to produce the same hash value.",
          "\n\nAs far as passwords go, SHA256 is one of the most recommended hashing methods to go with for security assurance.",
          "\n\nAn SHA256 hash is made by first adding a 'salt' to the plain-text input before hashing.",
          "\nA salt is just a random string of characters added to the beginning or end of the input to increase difficulty in cracking the hash.",
          "\nThen an algorithm is performed on the newly altered input to create our hash.",
          "\nAn SHA256 hash is always 64 digits long (256-bit; 232-byte)",
          "\n\nTry it for yourself now!\n")
    
    password = input("Input a common password to hash: ")
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha256(setpass)
    guess_pw = hash_object.hexdigest()

    print("Thanks! Now re-enter the password and we will compare them to see if they are the same!: ")

    second_password = input("Confirm the password: ")
    setpass = bytes(second_password, 'utf-8')
    hash_object = hashlib.sha256(setpass)
    confirm_pw = hash_object.hexdigest()

    print("\nHash of first entered password: ", guess_pw)
    print("Hash of second entered password: ", confirm_pw)

    if(guess_pw == confirm_pw):
        print("\nPasswords are the same")
        print("The hash values of the two passwords are the same")
    else:
        print("\nInvalid combination; passwords not the same")
        print("The hash values of the two passwords are NOT the same")


    print("\nGreat! Now that we can see how two passwords are comapared without them being in plain-text, let's try cracking the password!")
    print("\nCopy the hash value of one of the above passwords and paste it below. It's hacking time!")



    sha256hash = input("Please input the hash to crack: ")
    common_passwords = open("common_passwords.txt").read().splitlines()
    for guess in common_passwords:
        hashedGuess = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
        if(hashedGuess == sha256hash):
            print("The password is: ", str(guess))
            print("\nGreat! You hacked the password!",
                  "\nWhat happeneded here was the code took the hashed value and compared it to the hash values of a text file filled with the most common passwords in the world.",
                  "\nIf it found a match, it printed it out here in plaintext!",
                  "\n\nThis can be used practically by intercepting hashed password values and then applying this method to break them\n")
            break

    try:
        hash_mode = int(input("Type 1 to redo this hash type, 2 to go to another hash type, or 3 to exit, and press 'Enter': "))
    except ValueError:
        print("\nThat's not an integer... come on man please, you know what a number is\n")
        first_code()
        
    if(hash_mode == 1):
        sha256Crack()
    elif(hash_mode == 2):
        first_code()
    elif(hash_mode == 3):
        exit
    else:
        print("That wasn't an option, returning to hash types\n")
        first_code()






###MD5 Password Crack

def md5Crack():
    import hashlib
    import ctypes
    import urllib
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------------MD5------------------------------------------------------------------------\n")
    print("\nMD5 is one of the oldest hashing methods, and has been made obsolete by many other methods.",
          "\nIt has many security issues that make it undesirable for use, but it is still one of the most widely used methods in the world, purly out of tradition.",
          "\nOne of the security flaws is that it has an extremely high collision rate, meaning that two separate inputs can create the same hash value.",
          "\nThe main issue with MD5 is that it runs very quickly. While this may seems good at first, it means that it also runs very quickly for hackers.",
          "\nSince it runs at such a fast pace, hackers can try extremely high volumes of password cracks very quickly, which increases their likelyhood of success.",
          "\n\nDespite its wide use, using MD5 is highly discouraged, especially for password storage.",
          "\n\nAn MD5 hash is made by first adding a 'salt' to the plain-text input before hashing.",
          "\nA salt is just a random string of characters added to the beginning or end of the input to increase difficulty in cracking the hash.",
          "\nThen an algorithm is performed on the newly altered input to create our hash.",
          "\nAn MD5 hash is always 32 digits long (128-bit; 16-byte)",
          "\n\nTry it for yourself now!\n")
    
    password = input("Input a common password to hash: ")
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()

    print("Thanks! Now re-enter the password and we will compare them to see if they are the same!: ")

    second_password = input("Confirm the password: ")
    setpass = bytes(second_password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    confirm_pw = hash_object.hexdigest()

    print("\nHash of first entered password: ", guess_pw)
    print("Hash of second entered password: ", confirm_pw)

    if(guess_pw == confirm_pw):
        print("\nPasswords are the same")
        print("The hash values of the two passwords are the same")
    else:
        print("\nInvalid combination; passwords not the same")
        print("The hash values of the two passwords are NOT the same")


    print("\nGreat! Now that we can see how two passwords are comapared without them being in plain-text, let's try cracking the password!")
    print("\nCopy the hash value of one of the above passwords and paste it below. It's hacking time!")



    md5hash = input("Please input the hash to crack: ")
    common_passwords = open("common_passwords.txt").read().splitlines()
    for guess in common_passwords:
        hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if(hashedGuess == md5hash):
            print("The password is: ", str(guess))
            print("\nGreat! You hacked the password!",
                  "\nWhat happeneded here was the code took the hashed value and compared it to the hash values of a text file filled with the most common passwords in the world.",
                  "\nIf it found a match, it printed it out here in plaintext!",
                  "\n\nThis can be used practically by intercepting hashed password values and then applying this method to break them\n")
            break

    try:
        hash_mode = int(input("Type 1 to redo this hash type, 2 to go to another hash type, or 3 to exit, and press 'Enter': "))
    except ValueError:
        print("\nThat's not an integer... come on man please, you know what a number is\n")
        first_code()
        
    if(hash_mode == 1):
        md5Crack()
    elif(hash_mode == 2):
        first_code()
    elif(hash_mode == 3):
        exit
    else:
        print("That wasn't an option, returning to hash types\n")
        first_code()





def first_code():
    try:
        hash_mode = int(input("\nType 1 for SHA1, 2 for SHA256, 3 for MD5, 4 to exit, and press 'Enter': "))
    except ValueError:
        print("\nThat's not an integer... come on man please, you know what a number is\n")
        first_code()
        
    if(hash_mode == 1):
        sha1Crack()
    elif(hash_mode == 2):
        sha256Crack()
    elif(hash_mode == 3):
        md5Crack()
    elif(hash_mode == 4):
        exit
    else:
        print("That wasn't an option.\nLook man, I only had a day, 3 options was the best I could do!\n")
        first_code()


print("\nWelcome to the Brute Force Hash Hack!\n")

print("I made this code to help users visualize the 3 most common hash types",
      "\nThese hashes are SHA1, SHA256, and MD5",
      "\nA hash is used to make an input irreversibly unreadable to human eyes",
      "\nSince making the input unreadable via hashing is irreversible, hashes are commonly used for password protection!",
      "\n\nIt works by an algorithm taking an input (ex. your password) and jumbling it up to make it nonsensical to humans",
      "\nThen, in the case of passwords, the jumbled up version (AKA the hash) is stored in place of your plain-text password",
      "\nWhen you go to login to the account or website again, the password you login with is jumbled up using the same algorithm, and compared to the stored hash of your password",
      "\n\nUsing this same comparison method, we can hack simple and common passwords using what is called a 'Brute Force Attack'",
      "\nSince the hash is irreversible, we can instead compare the stored hash to the hash value of common passwords we know, and see if any of them fit",
      "\n\nThis may seem complicated in theory, but I hope this project makes the concept seem simple by the end!\n"
      "\n\nLet's get started")

first_code()




