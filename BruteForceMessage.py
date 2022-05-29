from time import sleep

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
MESSAGE = "PASSWORD UNLOCKED"

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
        #sleep(1)
        inSet += ALPHABET[j]
        j = 0
        i = i + 1
        print(inSet)
