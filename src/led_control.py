from hal import hal_led as led
from threading import Thread
from time import sleep
from hal import hal_keypad as keypad

def led_thread():
<<<<<<< HEAD
    global delay
    delay = 0 
    while(True):
        if delay != 0: 
            led.set_output(20,1) 
            sleep(delay)
            led.set_output(20, 0) 
            sleep(delay)

def led_control_init():
    global delay
    
    t1 = Thread(target=led_thread)
    t1.start()
    #Set initial LED blinking every 1 second after Thread starts 
    delay = 1
=======
 global delay
 delay = 0 
 while(True):
    if delay != 0: 
        led.set_output(20,1) 
        sleep(delay)
        led.set_output(20, 0) 
        sleep(delay)
    else:
        led.set_output(20,0)

def led_control_init():
 global delay
 led.init()
 t1 = Thread(target=led_thread)
 t1.start()
 #Set initial LED blinking every 1 second after Thread starts 
 delay = 0
>>>>>>> c76f47ac3117cfebc623379f1a0ba1b12a2d0cf6
