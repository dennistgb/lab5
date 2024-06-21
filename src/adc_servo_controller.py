from hal import hal_servo as servo
from hal import hal_adc as adc


def main():
    servo.init()
    adc.init()
    while(1):
        servo.set_servo_position(180)
        servo.set_servo_position(0)

    

def adjust():
    while(True):
        turn = adc.get_adc_value(1)
        print(turn)
        if adc.get_adc_value(1):
            servo.set_servo_position(turn/5.63)

if __name__ == "__main__":
    main()
