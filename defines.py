import types

RS = types.SimpleNamespace()
#race states
RS.un_init = "un_init";
RS.is_initializing = "is_initializing";
RS.standby = "standby";
RS.countdown5 = "countdown_5";
RS.waitcountdown5 = "waitcountdown5";
RS.countdown4 = "countdown_4";
RS.waitcountdown4 = "waitcountdown4";
RS.countdown3 = "countdown_3";
RS.waitcountdown3 = "waitcountdown3";
RS.countdown2 = "countdown_2";
RS.waitcountdown2 = "waitcountdown2";
RS.countdown1 = "countdown_1";
RS.waitcountdown1 = "waitcountdown1";
RS.countdowngo = "countdown_go";
RS.waitcountdowngo = "waitcountdowngo";
RS.playing = "playing";
RS.end_P1_win = "end_P1_win";
RS.end_P2_win = "end_P2_win";
RS.end_P3_win = "end_P3_win";
RS.end_P4_win = "end_P4_win";
RS.end_cancel = "end_cancel";
RS.waitwintunefinised = "waitwintunefinised";
RS.end_win_tune = "end_win_tune";
RS.error_init = "error_init";

TUNES = types.SimpleNamespace()
TUNES.camelsong = 1;
TUNES.countdown5 = 2;
TUNES.countdown4 = 3;
TUNES.countdown3 = 4;
TUNES.countdown2 = 5;
TUNES.countdown1 = 6;
TUNES.start = 7;
TUNES.punt1 = 8;
TUNES.punt2 = 9;
TUNES.punt3 = 10;
TUNES.punt4 = 11;
TUNES.winner1 = 12;
TUNES.winner2 = 13;
TUNES.winner3 = 14;
TUNES.winner4 = 15;


BITES = types.SimpleNamespace()
BITES.camelsong = "./sounds/kamelenrace_lang.wav";
BITES.countdown5 = "./sounds/countdown5.wav";
BITES.countdown4 = "./sounds/countdown4.wav";
BITES.countdown3 = "./sounds/countdown3.wav";
BITES.countdown2 = "./sounds/countdown2.wav";
BITES.countdown1 = "./sounds/countdown1.wav";
BITES.start = "./sounds/start1.wav";
BITES.punt1 = "./sounds/punt1.wav";
BITES.punt2 = "./sounds/punt2.wav";
#BITES.punt3 = "./sounds/punt3.wav";
BITES.punt3 = "./sounds/lins_okay_letsgo.wav";
#BITES.punt4 = "./sounds/punt4.wav";
BITES.punt4 = "./sounds/anne_yes_lekker.wav";
BITES.winner1 = "./sounds/winner1.wav";
BITES.winner2 = "./sounds/winner2.wav";
BITES.winner3 = "./sounds/winner3.wav";
BITES.winner4 = "./sounds/winner4.wav";



LIGHTS = types.SimpleNamespace()
#race states
LIGHTS.un_init = "un_init";
LIGHTS.is_initializing_p1 = "is_initializing_p1";
LIGHTS.is_initializing_p2 = "is_initializing_p2";
LIGHTS.is_initializing_p3 = "is_initializing_p3";
LIGHTS.is_initializing_p4 = "is_initializing_p4";
LIGHTS.standby_p1 = "standby_p1";
LIGHTS.standby_p2 = "standby_p2";
LIGHTS.standby_p3 = "standby_p3";
LIGHTS.standby_p4 = "standby_p4";
LIGHTS.countdown5 = "countdown_5";
LIGHTS.countdown4 = "countdown_4";
LIGHTS.countdown3 = "countdown_3";
LIGHTS.countdown2 = "countdown_2";
LIGHTS.countdown1 = "countdown_1";
LIGHTS.countdowngo = "countdown_go";
LIGHTS.playing = "playing";
LIGHTS.score_P1_gold    = "score_p1_3";
LIGHTS.score_P1_orange  = "score_p1_2";
LIGHTS.score_P1_blue    = "score_p1_1";
LIGHTS.score_P2_gold    = "score_p2_3";
LIGHTS.score_P2_orange  = "score_p2_2";
LIGHTS.score_P2_blue    = "score_p2_1";
LIGHTS.score_P3_gold    = "score_p3_3";
LIGHTS.score_P3_orange  = "score_p3_2";
LIGHTS.score_P3_blue    = "score_p3_1";
LIGHTS.score_P4_gold    = "score_p4_3";
LIGHTS.score_P4_orange  = "score_p4_2";
LIGHTS.score_P4_blue    = "score_p4_1";
LIGHTS.winner_p1 = "winner_p1";
LIGHTS.winner_p2 = "winner_p2";
LIGHTS.winner_p3 = "winner_p3";
LIGHTS.winner_p4 = "winner_p4";
