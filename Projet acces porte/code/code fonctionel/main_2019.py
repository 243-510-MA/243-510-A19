import time

import mail

import PAD as pad


# this stores the code of key box
doorPassword = "6220"


while True :
    
    while True :
    
        # get 7 inputs from the user to form their student ID
        # pressing the "#" key resets user input
        userId = [None,None,None,None,None,None,None]
        
        userId[0] = pad.bouton()    
        while(userId[0] == None) :
            userId[0] = pad.bouton()

        if (userId[0] == "#") :
            break
            
        userId[1] = pad.bouton()    
        while(userId[1] == None) :
            userId[1] = pad.bouton()
            
        if (userId[1] == "#") :
            break
            
        userId[2] = pad.bouton()    
        while(userId[2] == None) :
            userId[2] = pad.bouton()
        
        if (userId[2] == "#") :
            break
            
        userId[3] = pad.bouton()    
        while(userId[3] == None) :
            userId[3] = pad.bouton()

        if (userId[3] == "#") :
            break
            
        userId[4] = pad.bouton()    
        while(userId[4] == None) :
            userId[4] = pad.bouton()

        if (userId[4] == "#") :
            break
            
        userId[5] = pad.bouton()    
        while(userId[5] == None) :
            userId[5] = pad.bouton()

        if (userId[5] == "#") :
            break
            
        userId[6] = pad.bouton()    
        while(userId[6] == None) :
            userId[6] = pad.bouton()
        
        if (userId[6] == "#") :
            break
        

        # forms the email address to send the code of key box to
        userAddress = "e" + ''.join(userId) + "@cmaisonneuve.qc.ca"
        
        # sends an email to the address of the user whit the code of key box 
        mail.sendEmail(userAddress, doorPassword)

        

   
