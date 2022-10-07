import paho.mqtt.client as paho
import RPi.GPIO as GPIO
broker = "iotkmitl.ddns.net"
port = 9001
LED = 2
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED,0)


def on_message(mosq, obj, msg):
    global message
    print(msg.payload.decode("utf-8"))
    message = msg.payload.decode("utf-8")
    if (message == "on"):
        GPIO.output(LED,1)
    else:
        GPIO.output(LED,0)
def on_subscribe(mosq, obg, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    
def on_publish(client,userdata,result):
    print("data published \n")
    
client1 = paho.Client("control9",transport="websockets")
client1.username_pw_set(username="kmitlcie", password="ciehasmoney")
client1.on_publish = on_publish
client1.on_subscribe = on_subscribe
client1.on_message = on_message

client1.connect(broker,port)
ret = client1.publish("banana","on")

client1.subscribe("banana",0)
client1.loop_forever()