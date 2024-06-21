from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buz
from hal import hal_keypad as keypad

correct_pass = [1,2,3,4]
wrong_entries = 0
password = []
display = LCD.lcd()
display.lcd_clear()

def req1():
    display.lcd_display_string("Safe Lock",1)
    display.lcd_display_string("Enter PIN",2)

def req2(key):
    global password
    password.append(key)
    password_display = '*' * len(password)  # Convert to asterisks
    display.lcd_clear()
    display.lcd_display_string("Safe Lock",1)
    display.lcd_display_string(password_display, 2)
    print("Current password input:", password)
    if len(password) == 4:
         check_pass()
    
def check_pass():
    global password
    global wrong_entries
    if password == correct_pass:
        display.lcd_clear()
        display.lcd_display_string("Safe Unlocked",1)
        password.clear()
    elif wrong_entries > 2:
        display.lcd_clear()
        display.lcd_display_string("Safe Disabled",1)
        password.clear()
    elif password != correct_pass:
        display.lcd_clear()
        display.lcd_display_string("Wrong PIN")
        password.clear()
        wrong_entries += 1



def main():
    password.clear()
    req1()
    keypad.init(req2)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    



if __name__ == "__main__":
    main()



