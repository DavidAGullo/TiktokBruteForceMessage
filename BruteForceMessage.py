from time import sleep

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " #Characters Allowed for the script, it will cycle through these.
MESSAGE = "PASSWORD UNLOCKED" #The final output of the message, in Bruteforce fashion

#------------------------------------------------------#
# The Code                                             #
#------------------------------------------------------#
i = 0
j = 0
inSet = ""
while(True):
    if(inSet == MESSAGE):
        break
    elif(ALPHABET[j] != MESSAGE[i]):
        sleep(0.05)
        print(inSet + ALPHABET[j])
        j = j+1
    else:
        inSet += ALPHABET[j]
        j = 0
        i = i + 1
        print(inSet)
