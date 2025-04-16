import sys
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
import random
import paho.mqtt.client as mqtt
import time
from config import CONFIG
from time import sleep

#globalScore = 0
main = None;
mqttc = None;

#/KAMELEN/IN/KAMEEL1 [0-100]
#/KAMELEN/IN/KAMEEL2 [0-100]
#/KAMELEN/IN/KAMEEL3 [0-100]
#/KAMELEN/IN/KAMEEL4 [0-100]
#/KAMELEN/OUT/KAMEEL1_ISREADY [0-1]
#/KAMELEN/OUT/KAMEEL2_ISREADY [0-1]
#/KAMELEN/OUT/KAMEEL3_ISREADY [0-1]
#/KAMELEN/OUT/KAMEEL4_ISREADY [0-1]

class MainApplication():
    def __init__(self, master):

        self.parent = master;
        self.frame = tk.Frame(self.parent)
        self.frame.pack();
        #create gui here
        self.scorevar1= tk.StringVar();
        self.scorevar2= tk.StringVar();
        self.scorevar3= tk.StringVar();
        self.scorevar4= tk.StringVar();

        self.scorevar1.set("Kameel-1 [0]:")
        self.scorevar2.set("Kameel-2 [0]:")
        self.scorevar3.set("Kameel-3 [0]:")
        self.scorevar4.set("Kameel-4 [0]:")
        self.Iscorevar1 = tk.IntVar()
        self.Iscorevar2 = tk.IntVar()
        self.Iscorevar3 = tk.IntVar()
        self.Iscorevar4 = tk.IntVar()

        self.k1_lbl = tk.Label(textvariable=self.scorevar1)
        self.k1_pb1 = ttk.Progressbar(self.parent, orient=tk.HORIZONTAL, length=500, mode='determinate', variable=self.Iscorevar1)
        self.k2_lbl = tk.Label(textvariable=self.scorevar2)
        self.k2_pb1 = ttk.Progressbar(self.parent, orient=tk.HORIZONTAL, length=500, mode='determinate', variable=self.Iscorevar2)
        self.k3_lbl = tk.Label(textvariable=self.scorevar3)
        self.k3_pb1 = ttk.Progressbar(self.parent, orient=tk.HORIZONTAL, length=500, mode='determinate', variable=self.Iscorevar3)
        self.k4_lbl = tk.Label(textvariable=self.scorevar4)
        self.k4_pb1 = ttk.Progressbar(self.parent, orient=tk.HORIZONTAL, length=500, mode='determinate', variable=self.Iscorevar4)

        self.k1_lbl.pack()
        self.k1_pb1.pack()
        self.k2_lbl.pack()
        self.k2_pb1.pack()
        self.k3_lbl.pack()
        self.k3_pb1.pack()
        self.k4_lbl.pack()
        self.k4_pb1.pack()

        self.parent.wm_protocol("WM_DELETE_WINDOW", self.on_closing)
        self.close = 0

    def updateScore(self,camel, score):
        #global globalScore 
        #globalScore = globalScore + inc
        #global scorevar 
        if(camel==1):
            self.scorevar1.set("Kameel-1 ["+str(score)+"]:")
            self.k1_lbl.config(fg="red")
            self.Iscorevar1.set(score)
            #self.k1_pb1.step(score)

        elif(camel==2):
            self.scorevar2.set("Kameel-2 ["+str(score)+"]:")
            self.k2_lbl.config(fg="red")
            self.Iscorevar2.set(score)
            #self.k2_pb1.step(score)
        elif(camel==3):
            self.scorevar3.set("Kameel-3 ["+str(score)+"]:")
            self.k3_lbl.config(fg="red")
            self.Iscorevar3.set(score)
            #self.k3_pb1.step(score)
        elif(camel==4):
            self.scorevar4.set("Kameel-4 ["+str(score)+"]:")
            self.k4_lbl.config(fg="red")
            self.Iscorevar4.set(score)
            #self.k4_pb1.step(score)


    def on_closing(self):
        print( "Over")
        self.close = 1
 

 
class MyMQTTClass(mqtt.Client):
    

    def on_connect(self, mqttc, obj, flags, reason_code):
        print("rc: "+str(reason_code))

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        if self.f is not None:
            self.f(msg.topic, msg.payload);

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, reason_code_list):
        print("Subscribed: "+str(mid)+" "+str(reason_code_list))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def setup(self, name):
        f = None;
        self.mqttname = name;
        self.connect(CONFIG.MQTTSERVER, CONFIG.MQTTPORT, 10)
        self.subscribe(self.mqttname+"/IN/#", 0)

    def run(self):
        #rc = self.loop();
        self.loop_read()
        self.loop_write()
        rc = self.loop_misc()
        return rc

    def publishState(self, kameel, state):
        topic = self.mqttname+"/OUT"+kameel
        msg = f"{state}"
        result = self.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def ReplyIsUp(self):
        topic = self.mqttname+"/OUT/ISALIVE";
        result = self.publish(topic, "PING")
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send msg to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def my_message(name, payload):
    ##reset functionality
    global main
    value = int( payload.decode('UTF-8') ) 

    if( name.endswith("KAMEEL1")  ):
        if( (value > -1) & (value < 101) ):
            main.updateScore(1,value)
    if( name.endswith("KAMEEL2")  ):
        if( (value > -1) & (value < 101) ):
            main.updateScore(2,value)
    if( name.endswith("KAMEEL3")  ):
        if( (value > -1) & (value < 101) ):
            main.updateScore(3,value)
    if( name.endswith("KAMEEL4")  ):
        if( (value > -1) & (value < 101) ):
            main.updateScore(4,value)
    if( name.endswith("/SENDALIVE")  ):
        global mqttc
        mqttc.ReplyIsUp();
    print(name, payload)
    


if __name__ == "__main__":
    name= 'KAMELEN'
    argvlen = len(sys.argv);
    if(argvlen>1):
        first = sys.argv[0];
        secnd = sys.argv[1];
        print(first)
        print(secnd)
        name = secnd;

    root = tk.Tk();
    root.title(name)
    main = MainApplication(root)
    client_id = f'subscribe-{random.randint(0, 100)}'
    mqttc = MyMQTTClass(client_id)
    mqttc.setup(name)
    mqttc.f = my_message
    rc = 0;
    tscore = 0;
    timer1start = 0;
    timer2start = 0;
    timer3start = 0;
    timer4start = 0;
    while (main.close != 1) & (rc == 0):
        sleep(0.1)
        root.update();
        rc = mqttc.run();
        #rc =0
        #if(rc != 0):
        #    mqttc.reconnect()
        #    rc = mqttc.run();

        
        if((main.k1_lbl.cget("fg") == "red") ):
            main.k1_lbl.config(fg="orange")
            timer1start = time.time()
            mqttc.publishState("/KAMEEL1_ISREADY", 0) #0 = busy 1=idle
        if((main.k2_lbl.cget("fg") == "red")):
            main.k2_lbl.config(fg="orange")
            timer2start = time.time()
            mqttc.publishState("/KAMEEL2_ISREADY", 0) #10 = busy 1=idle
        if((main.k3_lbl.cget("fg") == "red") ):
            main.k3_lbl.config(fg="orange")
            timer3start = time.time()
            mqttc.publishState("/KAMEEL3_ISREADY", 0) #0 = busy 1=idle
        if((main.k4_lbl.cget("fg") == "red") ):
            main.k4_lbl.config(fg="orange")
            timer4start = time.time()
            mqttc.publishState("/KAMEEL4_ISREADY", 0) #0 = busy 1=idle
        
        
        if((main.k1_lbl.cget("fg") == "orange") & (time.time() > timer1start + 5)):
            main.k1_lbl.config(fg="green")
            timer1start = 0
            mqttc.publishState("/KAMEEL1_ISREADY", 1) #0 = busy 1=idle
            
        if((main.k2_lbl.cget("fg") == "orange") & (time.time() > timer2start + 5)):
            main.k2_lbl.config(fg="green")
            timer2start = 0
            mqttc.publishState("/KAMEEL2_ISREADY", 1) #0 = busy 1=idle
            
        if((main.k3_lbl.cget("fg") == "orange") & (time.time() > timer3start + 5)):
            main.k3_lbl.config(fg="green")
            timer3start = 0
            mqttc.publishState("/KAMEEL3_ISREADY", 1) #0 = busy 1=idle
            
        if((main.k4_lbl.cget("fg") == "orange") & (time.time() > timer4start + 5)):
            main.k4_lbl.config(fg="green")
            timer4start = 0
            mqttc.publishState("/KAMEEL4_ISREADY", 1) #0 = busy 1=idle


    print("rc: "+str(rc))