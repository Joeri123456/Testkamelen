import sys
import tkinter as tk
import tkinter.scrolledtext as st 
import random
import paho.mqtt.client as mqtt
from config import CONFIG
from time import sleep

globalScore = 0
main = None;
mqttc = None;

class MainApplication():
    def __init__(self, master):

        self.parent = master;
        self.frame = tk.Frame(self.parent)
        self.frame.pack();
        #create gui here
        self.scorevar= tk.StringVar();
        self.text_area = st.ScrolledText(root, 
                                width = 30,  
                                height = 8,  
                                font = ("Times New Roman", 
                                        15)) 
        self.scorevar.set("-")
        self.greeting = tk.Label(textvariable=self.scorevar)
        self.text_area.configure(state ='disabled') 
        self.button1 = tk.Button(
            text="Score 1 point",
            width=25,
            height=5,
            bg="blue",
            fg="yellow", 
            command=self.callback1
        )
        self.button2 = tk.Button(
            text="Score 2 points",
            width=25,
            height=5,
            bg="green",
            fg="yellow", 
            command=self.callback2
        )
        self.button3 = tk.Button(
            text="Score 3 points",
            width=25,
            height=5,
            bg="red",
            fg="yellow", 
            command=self.callback3
        )

        self.greeting.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.text_area.pack() 
        self.parent.wm_protocol("WM_DELETE_WINDOW", self.on_closing)
        self.close = 0

    def addScore(self,inc):
        global globalScore 
        globalScore = globalScore + inc
        #global scorevar 
        self.scorevar.set("Score: "+str(globalScore))
        self.text_area.configure(state ='normal') 
        self.text_area.insert(tk.END, '\n'+ 'Added '+str(inc)+' points. Global score: '+ str(globalScore) )
        self.text_area.see("end")
        self.text_area.configure(state ='disabled')    

    def callback1(self):
        self.addScore(1)

    def callback2(self):
        self.addScore(2)

    def callback3(self):
        self.addScore(3)

    def on_closing(self):
        print( "Over")
        self.close = 1
 
#/SPEELBAK1/OUT/SCORE [0-100]
#/SPEELBAK1/IN/RESET [NOW]
 
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

    def publishScore(self):
        global globalScore
        msg = f"{globalScore}"
        topic = self.mqttname+"/OUT/SCORE";
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
    if( name.endswith("/RESET")  ):
        if(payload.decode('UTF-8') == "NOW" ):
            print("payload matches")
            global globalScore
            globalScore  = 0;
            global main
            main.addScore(0)
    if( name.endswith("/SENDALIVE")  ):
        global mqttc
        mqttc.ReplyIsUp();
    print(name, payload)
    


if __name__ == "__main__":
    name= 'SPEELBAK1'
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
    while (main.close != 1) & (rc == 0):
        sleep(0.1)
        root.update();
        rc = mqttc.run();

        if tscore != globalScore:
            tscore = globalScore;
            mqttc.publishScore();


    print("rc: "+str(rc))