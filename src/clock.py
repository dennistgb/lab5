import time 
from hal import hal_lcd as LCD

def clock_thread():
    local_time = time.localtime() # get struct_time 
    global time_string
    time_string = time.strftime("%H:%M:%S", local_time) 

def main():
    display = LCD.lcd()
    display.lcd_clear()
    while(True):
        display.lcd_display_string(time_string,1)
        display.lcd_display_string("dd:mm:yyyy",2)

main()