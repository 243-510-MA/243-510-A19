import time

import RPi.GPIO as GPIO

# sets debounce delay (in secondes)
debounce = 0.5

# mapping the rasp's pins
# Physical pins of the PI is the first number (Ex: BTNE = 7)
BTNE = 7  #GPIO 4
BTN7 = 19 #GPIO 10
BTN4 = 21 #GPIO 9
BTN1 = 23 #GPIO 11
BTN0 = 29 #GPIO 5
BTN8 = 31 #GPIO 6
BTN5 = 37 #GPIO 26
BTN2 = 40 #GPIO 21
BTNH = 38 #GPIO 20
BTN9 = 32 #GPIO 12
BTN6 = 26 #GPIO 7
BTN3 = 24 #GPIO 8


# Setting each pin's mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BTNE , GPIO.IN)
GPIO.setup(BTN7 , GPIO.IN)
GPIO.setup(BTN4 , GPIO.IN)
GPIO.setup(BTN1 , GPIO.IN)
GPIO.setup(BTN0 , GPIO.IN)
GPIO.setup(BTN8 , GPIO.IN)
GPIO.setup(BTN5 , GPIO.IN)
GPIO.setup(BTN2 , GPIO.IN)
GPIO.setup(BTN9 , GPIO.IN)
GPIO.setup(BTN6 , GPIO.IN)
GPIO.setup(BTN3 , GPIO.IN)
GPIO.setup(BTNH , GPIO.IN)




#   description
#       converts digital input from the numpad into usable string
#
#   param
#       NONE
#
#   returns
#       a string containig the value of the button that has been pressed
#

def bouton() :
    
    if GPIO.input(BTNE):
        time.sleep(debounce)
        return "*"
        
    elif GPIO.input(BTN0):
        time.sleep(debounce)
        return "0"       
        
    elif GPIO.input(BTN1):
        time.sleep(debounce)
        return "1"
    
    elif GPIO.input(BTN2):
        time.sleep(debounce)
        return "2"
        
    elif GPIO.input(BTN3):
        time.sleep(debounce)
        return "3"
        
    elif GPIO.input(BTN4):
        time.sleep(debounce)
        return "4"
        
    elif GPIO.input(BTN5):
        time.sleep(debounce)
        return "5"
        
    elif GPIO.input(BTN6):
        time.sleep(debounce)
        return "6"
        
    elif GPIO.input(BTN7):
        time.sleep(debounce)
        return "7"
        
    elif GPIO.input(BTN8):
        time.sleep(debounce)
        return "8"
        
    elif GPIO.input(BTN9):
        time.sleep(debounce)
        return "9"
        
    elif GPIO.input(BTNH):
        time.sleep(debounce)
        return "#"
