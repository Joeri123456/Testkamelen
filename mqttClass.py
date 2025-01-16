import paho.mqtt.client as mqtt
from defines import CONFIG
import logging
logger = logging.getLogger("logfile")

class MyMQTTClass(mqtt.Client):
    
    def on_connect(self, mqttc, obj, flags, reason_code):
        logger.info("MQTT-rc: "+str(reason_code))

    def on_connect_fail(self, mqttc, obj):
        logger.error("MQTT-Connect failed")

    def on_message(self, mqttc, obj, msg):
        logger.debug("MQTT-"+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        if self.f is not None:
            self.f(msg.topic, msg.payload);

    def on_publish(self, mqttc, obj, mid):
        logger.debug("MQTT-published: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, reason_code_list):
        logger.info("MQTT-Subscribed: "+str(mid)+" "+str(reason_code_list))

    def on_log(self, mqttc, obj, level, string):
        logger.debug("MQTT-"+string)

    def setup(self, name):
        f = None;
        self.mqttname = name;
        self.connect(CONFIG.MQTTSERVER, CONFIG.MQTTPORT, 60)
        self.subscribe("SPEELBAK1/OUT/#", 0)
        self.subscribe("SPEELBAK2/OUT/#", 0)
        self.subscribe("SPEELBAK3/OUT/#", 0)
        self.subscribe("SPEELBAK4/OUT/#", 0)
        self.subscribe("KNOPPEN/OUT/#", 0)
        self.subscribe("KAMELEN/OUT/#", 0)

    def run(self):
        self.loop_read()
        self.loop_write()
        rc = self.loop_misc()
        return rc

    def publishTopic(self, topic, msg):
        _msg = f"{msg}"
        _topic = topic 
        result = self.publish(_topic, _msg)
        
        # result: [0, 1]
        status = result[0]
        if status == 0:
            logger.info("MQTT-"+f"Send `{_msg}` to topic `{_topic}`")
        else:
            logger.error("MQTT-"+f"Failed to send message to topic {_topic}")
