import time 
from hal import hal_lcd as LCD
from threading import Thread

def clock_thread():
    display = LCD.lcd()
    global time_string
    local_time = time.localtime() # get struct_time     
    time_string = time.strftime("%H:%M:%S", local_time) 
    print(time_string)
    display.lcd_display_string(f"timeis: {time_string}",1)

def main():
    display = LCD.lcd()
    display.lcd_clear()
    while(1):
        clock__thread = Thread(target=clock_thread())
        time.sleep(0.792)

if __name__ == "__main__":
    main()