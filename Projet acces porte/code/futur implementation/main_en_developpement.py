import time

from random import seed
from random import randint

import mail

import PAD as pad

seed("chaton")
doorPassword = randint(1000, 9999)# set it to 6220

adminId = "2917"

error_max = 3

# uncomment to show password
# print(doorPassword)

while 1 :

    error = 0

    # add clearscreen()
    print("howdy! who are u?")
    print("1 - student")
    print("2 - teacher")
    
    choiceRole = pad.bouton()
    while(choiceRole == None) :
        choiceRole = pad.bouton()
    #print(choiceRole)
    
    if choiceRole == "1" :  # ------------------------------------------------- student

        # add clearscreen()
        print("enter student id")
        
        userId = [None,None,None,None,None,None,None]
        #for i in range,(0, 6):
        userId[0] = pad.bouton()    
        while(userId[0] == None) :
            userId[0] = pad.bouton()
        userId[1] = pad.bouton()    
        while(userId[1] == None) :
            userId[1] = pad.bouton()
        userId[2] = pad.bouton()    
        while(userId[2] == None) :
            userId[2] = pad.bouton()
        userId[3] = pad.bouton()    
        while(userId[3] == None) :
            userId[3] = pad.bouton()
        userId[4] = pad.bouton()    
        while(userId[4] == None) :
            userId[4] = pad.bouton()
        userId[5] = pad.bouton()    
        while(userId[5] == None) :
            userId[5] = pad.bouton()
        userId[6] = pad.bouton()    
        while(userId[6] == None) :
            userId[6] = pad.bouton()
                
        #print(''.join(userId))     
        userAddress = "e" + ''.join(userId) + "@cmaisonneuve.qc.ca"
        
        # send mail
        mail.sendEmail(userAddress, doorPassword)

        # add clearscreen()
        print("an email has been sent to " + userAddress)
        print("enter password")
        print("Tries left : " + str(error_max))
        
        while error < 3 :
        
            userPass = [None,None,None,None]
            userPass[0] = pad.bouton()    
            while(userPass[0] == None) :
                userPass[0] = pad.bouton()
            userPass[1] = pad.bouton()    
            while(userPass[1] == None) :
                userPass[1] = pad.bouton()
            userPass[2] = pad.bouton()    
            while(userPass[2] == None) :
                userPass[2] = pad.bouton()
            userPass[3] = pad.bouton()    
            while(userPass[3] == None) :
                userPass[3] = pad.bouton()
                
            if ''.join(userPass) == str(doorPassword) :

                # add clearscreen()
                print("Congrats")
                # TODO add the part that opens the door
                time.sleep(10)
                break
                
            elif error < error_max - 1 :

                # add clearscreen()
                print("Nope that's not it")
                print("Enter your password : ")
                print("Tries left : " + str(error_max - 1 - error))
                error -=- 1

            else :

                # add clearscreen()
                print("You failed.")
                time.sleep(1)
                # add clearscreen()
                print("Miserably.")
                time.sleep(2)
                # add clearscreen()
                print("Try again in 10 secondes")
                time.sleep(10)
                break
            
    elif choiceRole == "2" :    # --------------------------------------------- teacher

        # add clearscreen()
        print("enter admin id")
        
        adminPass = [None,None,None,None]
        adminPass[0] = pad.bouton()    
        while(adminPass[0] == None) :
            adminPass[0] = pad.bouton()
        adminPass[1] = pad.bouton()    
        while(adminPass[1] == None) :
            adminPass[1] = pad.bouton()
        adminPass[2] = pad.bouton()    
        while(adminPass[2] == None) :
            adminPass[2] = pad.bouton()
        adminPass[3] = pad.bouton()    
        while(adminPass[3] == None) :
            adminPass[3] = pad.bouton()
        
        if ''.join(adminPass) == adminId :

            # add clearscreen()
            print("what do u wanna do?")
            print("1 - enter tha thing")
            print("2 - reset student password")

            choiceAction = pad.bouton()
            while(choiceAction == None) :
                choiceAction = pad.bouton()

            if choiceAction == "1" :

                # add clearscreen()
                print("Congrats")
                # TODO add the part that opens the door
                time.sleep(10)

            elif choiceAction == "2" :

                doorPassword = randint(1000, 9999)
                print("new password is : " + str(doorPassword))
                print("are you happy with the new password ?")
                print("1 - yes")
                print("2 - no")
                
                happiness = pad.bouton()
                while(happiness == None) :
                    happiness = pad.bouton()

                while happiness != "1" :
                    
                    doorPassword = randint(1000, 9999)
                    print("new password is : " + str(doorPassword))
                    print("are you happy with the new password ?")
                    print("1 - yes")
                    print("2 - no")

                    happiness = pad.bouton()
                    while(happiness == None) :
                        happiness = pad.bouton()
                
                
                # add clearscreen
                print("do u wanna enter ?")
                print("1 - yes")
                print("2 - no")
                
                entry = pad.bouton()
                while(entry == None) :
                    entry = pad.bouton()
                    
                if entry == "1" :

                    # add clearscreen()
                    print("Congrats")
                    # TODO add the part that opens the door
                    time.sleep(10)

                else : # fail safe

                    print("aight, cya")
                    time.sleep(10)

            else :  # fail safe

                print("plz enter a valid option")
                time.sleep(2)

        else : # fail safe

            print("plz enter a valid id")
            time.sleep(2)
       
    else :  # fail safe ------------------------------------------------------- major fuck up

        print("plz enter a valid option")
        time.sleep(2)





