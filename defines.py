import types

RS = types.SimpleNamespace()
#race states
RS.un_init = "un_init";
RS.is_initializing = "is_initializing";
RS.standby = "standby";
RS.countdown5 = "countdown5";
RS.waitcountdown5 = "waitcountdown5";
RS.countdown4 = "countdown4";
RS.waitcountdown4 = "waitcountdown4";
RS.countdown3 = "countdown3";
RS.waitcountdown3 = "waitcountdown3";
RS.countdown2 = "countdown2";
RS.waitcountdown2 = "waitcountdown2";
RS.countdown1 = "countdown1";
RS.waitcountdown1 = "waitcountdown1";
RS.countdowngo = "countdowngo";
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
