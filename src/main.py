from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control as LED

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()


#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    
    if key==1: 
        lcd.lcd_clear()
        lcd.lcd_display_string("LED control",1)
        lcd.lcd_display_string("Blink LED",2)
        LED.delay = 1
        

    elif key ==0:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control",1)
        lcd.lcd_display_string("OFF LED",2)
        LED.delay = 0

    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()
    LED.delay = 0
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)
    
    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    LED.led_control_init()


# Main entry point
if __name__ == "__main__":
    main()
