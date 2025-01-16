from Vars import myVars
from defines import RS, TUNES
from datetime import datetime
from logging.handlers import RotatingFileHandler
from soundmanager import SoundManager
import logging
logger = logging.getLogger("logfile")

def main():
    vars = myVars();
    Sounds = SoundManager();
    rc = 0;
    dt = 0;

    logger.info('Starting main while lus.')

    while (rc == 0):
        rc = vars.run();
        #RS.countdown1
        # statemachine loop
        match vars.state:
            case RS.un_init: #UNINIT
                if(vars.start_pressed): # wait for start button being pressed.
                    #Home kamelen
                    vars.setkameel1(0)
                    vars.setkameel2(0)
                    vars.setkameel3(0)
                    vars.setkameel4(0)
                    vars.state = RS.is_initializing

            case RS.is_initializing: # initializing racer
                if(vars.kameel1_isready & vars.kameel2_isready & vars.kameel3_isready & vars.kameel4_isready):
                   # all camels initialized.
                   vars.state = RS.standby
                   vars.start_pressed 

            case RS.standby:
                if(vars.start_pressed): # wait for start button being pressed.
                    vars.state = RS.countdown5
                    
            case RS.countdown5:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdown5
                Sounds.starttune(TUNES.countdown5)

            case RS.waitcountdown5:
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying() ): # wait for 1 seconds has passed.
                    vars.state = RS.countdown4
                     
            case RS.countdown4:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdown4
                Sounds.starttune(TUNES.countdown4)

            case RS.waitcountdown4:
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wait for 1 seconds has passed.
                    vars.state = RS.countdown3
                                                   
            case RS.countdown3:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdown3
                Sounds.starttune(TUNES.countdown3)

            case RS.waitcountdown3:
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wait for 1 seconds has passeded.
                    vars.state = RS.countdown2
                     
            case RS.countdown2:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdown2
                Sounds.starttune(TUNES.countdown2)

            case RS.waitcountdown2:
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wait for 1 seconds has passed.
                    vars.state = RS.countdown1                    
                     
            case RS.countdown1:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdown1
                Sounds.starttune(TUNES.countdown1)

            case RS.waitcountdown1:
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wwait for 1 seconds has passed.
                    vars.state = RS.countdowngo
                     
            case RS.countdowngo:
                dt = datetime.now().timestamp() # trigger counter
                vars.state = RS.waitcountdowngo 
                Sounds.starttune(TUNES.start)

            case RS.waitcountdowngo:
                vars.resetspeelbak1("NOW")
                vars.resetspeelbak2("NOW")
                vars.resetspeelbak3("NOW")
                vars.resetspeelbak4("NOW")
                vars.winner = 0
                #if( (vars.getspeelbak1_score ==0) & (vars.getspeelbak2_score ==0) & (vars.getspeelbak3_score ==0) & (vars.getspeelbak4_score ==0))
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wwait for 1 seconds has passed.
                    vars.state = RS.playing # wait for sound to finish.
                    Sounds.starttune(TUNES.camelsong)

            case RS.playing:
                if(vars.speelbak1_score  >= vars.maxscore):
                    vars.winner = 1
                    vars.state = RS.end_P1_win
                elif(vars.speelbak2_score >= vars.maxscore):
                    vars.winner = 2
                    vars.state = RS.end_P2_win
                elif(vars.speelbak3_score >= vars.maxscore):
                    vars.winner = 3
                    vars.state = RS.end_P3_win
                elif(vars.speelbak4_score >= vars.maxscore):
                    vars.winner = 4
                    vars.state = RS.end_P4_win
                
                if(vars.speelbak1_hasscored):
                    vars.setkameel1(vars.speelbak1_score)
                    Sounds.starttune(TUNES.punt1)
                if(vars.speelbak2_hasscored):
                    vars.setkameel2(vars.speelbak2_score)
                    Sounds.starttune(TUNES.punt2)
                if(vars.speelbak3_hasscored):
                    vars.setkameel3(vars.speelbak3_score)
                    Sounds.starttune(TUNES.punt3)
                if(vars.speelbak4_hasscored):
                    vars.setkameel4(vars.speelbak4_score)
                    Sounds.starttune(TUNES.punt4)
                
            
            case RS.end_P1_win:
                # set win tune for player
                dt = datetime.now().timestamp() # trigger counter
                Sounds.starttune(TUNES.winner1)
                # set animation
                vars.state = RS.waitwintunefinised

            case RS.end_P2_win:
                # set win tune for player
                dt = datetime.now().timestamp() # trigger counter
                Sounds.starttune(TUNES.winner2)
                # set animation
                vars.state = RS.waitwintunefinised

            case RS.end_P3_win:
                # set win tune for player
                dt = datetime.now().timestamp() # trigger counter
                Sounds.starttune(TUNES.winner3)
                # set animation
                vars.state = RS.waitwintunefinised

            case RS.end_P4_win:
                # set win tune for player
                dt = datetime.now().timestamp() # trigger counter
                Sounds.starttune(TUNES.winner4)
                # set animation
                vars.state = RS.waitwintunefinised

            case RS.waitwintunefinised:
                # if tune finished
                if( (dt+5) < datetime.now().timestamp() or not Sounds.tuneisplaying()): # wwait for 1 seconds has passed.
                    vars.state = RS.un_init
                                
            case _:
                print("Unhandled statemachine state", vars.state)

        if(vars.reset_pressed):
            #reset has been pressed set to uninit
            vars.resetspeelbak1("NOW")
            vars.resetspeelbak2("NOW")
            vars.resetspeelbak3("NOW")
            vars.resetspeelbak4("NOW")
            vars.state = RS.un_init

    logger.critical("rc: "+str(rc))


def initlog():
    # create logger with 'spam_application'
    logger = logging.getLogger("logfile")
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    #fh = logging.FileHandler('__main__.log')
    fh = RotatingFileHandler("logfile"+'.log', mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warning('warn message')
    #logger.error('error message')
    #logger.critical('critical message')

if __name__ == "__main__":
    initlog()
    main()