from machine import Pin, PWM
import time

#detection
ldr=Pin(19, Pin.IN)

#dc motor
in1=Pin(27, Pin.OUT)
in2=Pin(26, Pin.OUT)
ena=PWM(Pin(14, Pin.OUT))
ena.freq(1000)
#mouth
mouth_servo=PWM(Pin(13))
mouth_servo.freq(20)

#eyes
servo=PWM(Pin(5))
ir1=Pin(18, Pin.IN, Pin.PULL_UP)
ir2=Pin(4, Pin.IN, Pin.PULL_UP)
servo.freq(50)


trig=False
end_time = 0

#ENTIRE CODE BLOCK
while True:
    ldr_val=ldr.value()
    print("LDR:", ldr_val)
    ir1_val=ir1.value()
    ir2_val=ir2.value()
    print("IR1 ", ir1_val)
    print("IR2 ", ir2_val)
    time.sleep(0.5)
            #Mouth Servo
    for i in range(20, 37,4):
        mouth_servo.duty(i)
        time.sleep(0.3)
    for i in range(37,20 ,-4):
        mouth_servo.duty(i)
        time.sleep(0.3)
        
            #left eye
    if ir1_val==0:
        for i in range(70,50,-5):
            servo.duty(i)
            time.sleep(0.5)
        time.sleep(1)
        for i in range(50,70,5):
            servo.duty(i)
            time.sleep(0.5)
                
            #right eye
    elif ir2_val==0:
        for i in range(35,50,5):
            servo.duty(i)
            time.sleep(0.5)
            print("SIDE 1:", i)
        time.sleep(1)
        for i in range(50,35,-5):
            servo.duty(i)
            time.sleep(0.5)
    if ldr_val==1 and not trig:
        #makes thingy run only once cuz condition stays unsatisfied
        trig=True
        end_time = time.ticks_add(time.ticks_ms(), 60000)
        #Timer
        print("Time left", time.ticks_diff(end_time, time.ticks_ms())/1000)
        time.sleep(1)
        if time.ticks_diff(end_time, time.ticks_ms()) > 0:
            
            #DC MOTOR STARTS
            ena.duty(512)
            in1.value(1)
            in2.value(0)
            time.sleep(1)
        else:
            print("60 seconds finished. Stopping. Cooling down")
            ena.duty(0)
            trig=False
            
                
            
        
            
            