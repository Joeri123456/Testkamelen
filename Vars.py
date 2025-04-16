import random
from mqttClass import MyMQTTClass
from defines import RS
import logging
logger = logging.getLogger("logfile")


class myVars:
    def __init__(self):
        self.name= 'GAMECONTROLLER'
        self.client_id = f'subscribe-{random.randint(0, 100)}'
        self.mqttc = MyMQTTClass(self.client_id)
        self.mqttc.setup(self.name)
        self.mqttc.f = self.my_message
        self._state = RS.un_init
        self._kameel1_score = 0
        self._kameel2_score = 0
        self._kameel3_score = 0
        self._kameel4_score = 0
        self._kameel1_isready = 0
        self._kameel2_isready = 0
        self._kameel3_isready = 0
        self._kameel4_isready = 0
        self._start_pressed = False
        self._reset_pressed = False
        
        self._winner = 0
        self.maxscore = 20
        self._speelbak1_score = 0
        self._speelbak2_score = 0
        self._speelbak3_score = 0
        self._speelbak4_score = 0

        self._speelbak1_hasscored = False
        self._speelbak2_hasscored = False
        self._speelbak3_hasscored = False
        self._speelbak4_hasscored = False

    def getstate(self):
        return self._state
    def setstate(self, value):
        self._state = value
        self.mqttc.publishTopic(self.name+"/OUT/STATE", value)
    state = property(getstate, setstate, "")

    def getwinner(self):
        return self._winner
    def setwinner(self, value):
        self._winner = value
        self.mqttc.publishTopic(self.name+"/OUT/WINNER", value)
    winner = property(getwinner, setwinner, "")

    def getkameel1_isready(self):
        return self._kameel1_isready
    kameel1_isready = property(getkameel1_isready, "")

    def getkameel2_isready(self):
        return self._kameel2_isready   
    kameel2_isready = property(getkameel2_isready, "")

    def getkameel3_isready(self):
        return self._kameel3_isready    
    kameel3_isready = property(getkameel3_isready, "")

    def getkameel4_isready(self):
        return self._kameel4_isready  
    kameel4_isready = property(getkameel4_isready, "")

    def getresetpressed(self):
        temp = self._reset_pressed
        self._reset_pressed = False
        return temp  
    reset_pressed = property(getresetpressed, "")

    def getstartpressed(self):
        temp = self._start_pressed
        self._start_pressed = False
        return temp  
    start_pressed = property(getstartpressed, "")

    def getspeelbak1_score(self):
        return self._speelbak1_score  
    speelbak1_score = property(getspeelbak1_score, "")

    def getspeelbak2_score(self):
        return self._speelbak2_score  
    speelbak2_score = property(getspeelbak2_score, "")

    def getspeelbak3_score(self):
        return self._speelbak3_score  
    speelbak3_score = property(getspeelbak3_score, "")

    def getspeelbak4_score(self):
        return self._speelbak4_score  
    speelbak4_score = property(getspeelbak4_score, "")

    def getspeelbak1_hasscored(self):
        temp = self._speelbak1_hasscored
        self._speelbak1_hasscored = False
        return temp
    speelbak1_hasscored = property(getspeelbak1_hasscored, "")

    def getspeelbak2_hasscored(self):
        temp = self._speelbak2_hasscored
        self._speelbak2_hasscored = False
        return temp 
    speelbak2_hasscored = property(getspeelbak2_hasscored, "")

    def getspeelbak3_hasscored(self):
        temp = self._speelbak3_hasscored
        self._speelbak3_hasscored = False
        return temp
    speelbak3_hasscored = property(getspeelbak3_hasscored, "")

    def getspeelbak4_hasscored(self):
        temp = self._speelbak4_hasscored
        self._speelbak4_hasscored = False
        return temp
    speelbak4_hasscored = property(getspeelbak4_hasscored, "")

    def setkameel1(self, value):
        self.mqttc.publishTopic("KAMELEN/IN/KAMEEL1", value)
    def setkameel2(self, value):
        self.mqttc.publishTopic("KAMELEN/IN/KAMEEL2", value)
    def setkameel3(self, value):
        self.mqttc.publishTopic("KAMELEN/IN/KAMEEL3", value)
    def setkameel4(self, value):
        self.mqttc.publishTopic("KAMELEN/IN/KAMEEL4", value)

    def resetspeelbak1(self, value):
        self._speelbak1_score=0
        self.mqttc.publishTopic("SPEELBAK1/IN/RESET", value)
    def resetspeelbak2(self, value):
        self._speelbak2_score=0
        self.mqttc.publishTopic("SPEELBAK2/IN/RESET", value)
    def resetspeelbak3(self, value):
        self._speelbak3_score=0
        self.mqttc.publishTopic("SPEELBAK3/IN/RESET", value)
    def resetspeelbak4(self, value):
        self._speelbak4_score=0
        self.mqttc.publishTopic("SPEELBAK4/IN/RESET", value)

    def run(self):
        return self.mqttc.run();

    def my_message(self, name, payload):
        value = str( payload.decode('UTF-8') ) 

        if( name.endswith("GAMECONTROLLER/STATE") ):
            self._state = value
        elif( name.endswith("KAMEEL1_ISREADY") ):
            self._kameel1_isready = int(value)
        elif( name.endswith("KAMEEL2_ISREADY") ):
            self._kameel2_isready = int(value)
        elif( name.endswith("KAMEEL3_ISREADY") ):
            self._kameel3_isready = int(value)
        elif( name.endswith("KAMEEL4_ISREADY") ):
            self._kameel4_isready = int(value)
        elif( name.endswith("KAMELEN/OUT/ISALIVE") ):
            pass
        elif( name.endswith("KNOPPEN/OUT/CMD") ):
            if(value == "START"): self._start_pressed = True
            if(value == "RESET"): self._reset_pressed = True
        elif( name.endswith("KNOPPEN/OUT/ISALIVE") ):
            pass
        elif( name.endswith("SPEELBAK1/OUT/SCORE") ):
            _value = int(value)
            self._speelbak1_hasscored = (_value > self._speelbak1_score)
            self._speelbak1_score = _value
        elif( name.endswith("SPEELBAK1/OUT/ISALIVE") ):
            pass
        elif( name.endswith("SPEELBAK2/OUT/SCORE") ):
            _value = int(value)
            self._speelbak2_hasscored = (_value > self._speelbak2_score)
            self._speelbak2_score = _value
        elif( name.endswith("SPEELBAK2/OUT/ISALIVE") ):
            pass
        elif( name.endswith("SPEELBAK3/OUT/SCORE") ):
            _value = int(value)
            self._speelbak3_hasscored = (_value > self._speelbak3_score)
            self._speelbak3_score = _value
        elif( name.endswith("SPEELBAK3/OUT/ISALIVE") ):
            pass
        elif( name.endswith("SPEELBAK4/OUT/SCORE") ):
            _value = int(value)
            self._speelbak4_hasscored = (_value > self._speelbak4_score)
            self._speelbak4_score = _value
        elif( name.endswith("SPEELBAK4/OUT/ISALIVE") ):
            pass
        else:
            #logger.info("MQTT-"+f"Send `{_msg}` to topic `{_topic}`")
            logger.error("Unknown name: "+f"'{name}' '{value}'")
        logger.info("received message: "+f"'{name}' '{value}'")
    