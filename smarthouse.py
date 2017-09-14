import fbchat
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.output(3,False)
gpio.output(5,False)
gpio.output(7,False)
gpio.output(8,False)
client = fbchat.Client("thakukadri@housat.com", "********")   #username and password
friends = client.getUsers("Pi Rasp")                          #friends name
friend = friends[0]
last_messages = client.getThreadInfo(friend.uid,0)
local=last_messages[0].body
while(True):
    tag=0
    last_messages = client.getThreadInfo(friend.uid,0)
    if(local!=last_messages[0].body and last_messages[0].body!="wrong command" and last_messages[0].body.count("executed")==0):
        local=last_messages[0].body
        if(local=="white_on"):
            gpio.output(3,True)
        elif(local=="white_off"):
            gpio.output(3,False)
        elif(local=="blue_on"):
            gpio.output(5,True)
        elif(local=="blue_off"):
            gpio.output(5,False)
        elif(local=="green_on"):
            gpio.output(7,True)
        elif(local=="green_off"):
            gpio.output(7,False)
        elif(local=="red_on"):
            gpio.output(8,True)
        elif(local=="red_off"):
            gpio.output(8,False)
        elif(local=="power_off"):
            gpio.output(3,False)
            gpio.output(5,False)
            gpio.output(7,False)
            gpio.output(8,False)
        elif(local=="shutdown"):
            client.send(friend.uid, "shuting down")
            print("**************************************")
            print("shuting down")
            print("**************************************")
            break
        else:
             tag=1
        if(tag==0):
            temp="executed "+local
        else:
             temp="wrong command"
        sent=client.send(friend.uid, temp)
        if sent:
            print("**************************************")
            print(temp)
            print("**************************************")
gpio.cleanup()
