from machine import Pin, PWM
import time

#INITIALISING
ldr=Pin(35, Pin.IN)
#dc_automata
in1=Pin(18, Pin.OUT)
in2=Pin(14, Pin.OUT)
ena=PWM(Pin(21, Pin.OUT))

ena.freq(1000)
trig=False

#CODE BLOCK
while True:
    
    ldr_val=ldr.value()
    print(ldr_val)
    time.sleep(0.5)
    if ldr_val==1 and not trig:
        #makes thingy run only once cuz condition stays unsatisfied
        trig=True
        #DC MOTOR STARTS
        ena.duty(512)
        in1.value(1)
        in2.value(0)
        time.sleep(1)
        
        
        
    