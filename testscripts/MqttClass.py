#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This example shows how you can use the MQTT client in a class.

#import context  # Ensures paho is in PYTHONPATH
import random
import paho.mqtt.client as mqtt


class MyMQTTClass(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, reason_code):
        print("rc: "+str(reason_code))

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid, reason_codes):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, reason_code_list):
        print("Subscribed: "+str(mid)+" "+str(reason_code_list))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def setup(self):
        self.connect("localhost", 1883, 60)
        self.subscribe("python/#", 0)

        #rc = 0
        #while rc == 0:
        #    rc = self.loop()
        #return rc
    
    def run(self):
        rc = self.loop();
        return rc


client_id = f'subscribe-{random.randint(0, 100)}'
mqttc = MyMQTTClass(client_id)
mqttc.setup()
rc = 0;
while rc == 0:
    rc = mqttc.run();

print("rc: "+str(rc))