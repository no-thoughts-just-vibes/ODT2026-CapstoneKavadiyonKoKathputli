from machine import Pin, PWM
import time

#detection
laser = PWM(Pin(32))
ldr=Pin(5, Pin.IN)
laser.freq(1000)

#dc_automata
in1=Pin(33, Pin.OUT)
in2=Pin(32, Pin.OUT)
ena=PWM(Pin(14, Pin.OUT))
ena.freq(1000)
trig=False

#eyes
servo=PWM(Pin(4))
ir1=Pin(18, Pin.IN, Pin.PULL_UP)
ir2=Pin(19, Pin.IN, Pin.PULL_UP)
servo.freq(50)
irtrig1=False
irtrig2=False


#FN FOR LASER BRIGHTNESS
def set_brightness(percent):
    duty = int((percent / 100) * 1023)
    laser.duty(duty)

#CODE BLOCK
while True:
    set_brightness(100)
    ldr_val=ldr.value()
    ir1_val=ir1.value()
    ir2_val=ir2.value()
    print("IR1:", ir1_val)
    print("IR2:", ir2_val)
    print("LDR:", ldr_val)
    time.sleep(1)
    if ldr_val==1 and not trig:
        #makes thingy run only once cuz condition stays unsatisfied
        trig=True
        print("DC MOTOR STARTS")
        ena.duty(512)
        in1.value(1)
        in2.value(0)
        time.sleep(1)
        
    #left
    if ir1_val==0 and not irtrig1:
        irtrig1=True
        for i in range(35,70,5):
            servo.duty(i)
            time.sleep(0.05)
        print("Eye go left")
        irtrig1=False
        
    #right
    elif ir2_val==0 and not irtrig2:
        irtrig2=True
        for i in range(70,35,-5):
            servo.duty(i)
            time.sleep(0.05)
        print("Eye go right")
        irtrig2=False
        