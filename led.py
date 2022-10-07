import RPi.GPIO as GPIO
import time
import signal
import sys
import _thread

LED_OUT_1 = 2
LED_OUT_2 = 3
LED_OUT_3 = 4
LED_OUT_red = 13
LED_OUT_green = 6
BUTTON_IN = 19
count = 0

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup (LED_OUT_1, GPIO.OUT)
GPIO.setup (LED_OUT_2, GPIO.OUT)
GPIO.setup (LED_OUT_3, GPIO.OUT)
GPIO.setup (LED_OUT_red, GPIO.OUT)
GPIO.setup (LED_OUT_green, GPIO.OUT)

GPIO.output(LED_OUT_1, True)
GPIO.output(LED_OUT_2, True)
GPIO.output(LED_OUT_3, True)
GPIO.output(LED_OUT_red, False)

GPIO.setup(BUTTON_IN, GPIO.IN)

def button_iqr(ch):
    global count;
    #while True:
    #print(i)

    count = count + 1
    if (count>7):
        count = 0
        print(count)
    if(count==0):
        GPIO.output(LED_OUT_1, True)
        GPIO.output(LED_OUT_2, True)
        GPIO.output(LED_OUT_3, True)
        time.sleep(0.5);
    if(count==1):
        GPIO.output(LED_OUT_1, False)
        GPIO.output(LED_OUT_2, True)
        GPIO.output(LED_OUT_3, True)
        time.sleep(0.5);
    if(count==2):
        GPIO.output(LED_OUT_1, True)
        GPIO.output(LED_OUT_2, False)
        GPIO.output(LED_OUT_3, True)
        time.sleep(0.5);
    if(count==3):
        GPIO.output(LED_OUT_1, True)
        GPIO.output(LED_OUT_2, True)
        GPIO.output(LED_OUT_3, False)
        time.sleep(0.5);
    if(count==4):
        GPIO.output(LED_OUT_1, False)
        GPIO.output(LED_OUT_2, False)
        GPIO.output(LED_OUT_3, True)
        time.sleep(0.5);
    if(count==5):
        GPIO.output(LED_OUT_1, False)
        GPIO.output(LED_OUT_2, True)
        GPIO.output(LED_OUT_3, False)
        time.sleep(0.5);
    if(count==6):
        GPIO.output(LED_OUT_1, True)
        GPIO.output(LED_OUT_2, False)
        GPIO.output(LED_OUT_3, False)
        time.sleep(0.5);
    if(count==7):
        GPIO.output(LED_OUT_1, False)
        GPIO.output(LED_OUT_2, False)
        GPIO.output(LED_OUT_3, False)
        time.sleep(0.5);
           
GPIO.add_event_detect(BUTTON_IN, GPIO.RISING, callback=button_iqr, bouncetime=200)    

def thread1_def():
    green = GPIO.PWM(LED_OUT_green, 100)
    green.start(0)
    pause_time = 2
    run = 0
    while 1:
        run += 10
        green.ChangeDutyCycle(run)
        time.sleep(pause_time)
        if (run>=100):
            run = 0
        
    GPIO.output(LED_OUT_green, GPIO.HIGH)
    
_thread.start_new_thread(thread1_def,())
#time.sleep(1)
#GPIO.output(led, GPIO.HIGH)
    
while True:
    GPIO.output(13, True)
    time.sleep(1);
    GPIO.output(13, False)
    time.sleep(1);