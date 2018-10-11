#!/usr/bin/python3
#############################################################
# AUTHOR: Loopzen
# DATE: 2018-10-09
# DESCRIPTION: Pomodoro timer to polybar
# - Counter of all your completed pomodoros
# - Desktop notifications
# REQUERIMENTS:
# - polybar
# - dunst
# - fontAwesome
#############################################################
import time
import os
import sys

def kill_another_instances():
    os.system('pgrep pomobar > pomobar.pid')
    filePids = open("pomobar.pid", "r")
    for pidFile in filePids:
        pidFile = int(pidFile)
        if pidFile != int (os.getpid()) :
            os.system("kill -9 " + str(pidFile))
    filePids.close()
    os.system('rm pomobar.pid')

def increment_global_pomodoro_counter():
    # Read
    filePomodoroCounter = open(".pomodoroCounter", "r")
    pomodorosAcumulados = filePomodoroCounter.readline()
    filePomodoroCounter.close()
    # Increment
    pomodorosAcumulados = int(pomodorosAcumulados) + 1
    # Write
    filePomodoroCounter = open(".pomodoroCounter", "w")
    filePomodoroCounter.write(str(pomodorosAcumulados));
    filePomodoroCounter.close()

def get_pomodoros_done():
    filePomodoroCounter = open(".pomodoroCounter", "r")
    pomodorosAcumulados = filePomodoroCounter.read()
    filePomodoroCounter.close()
    return pomodorosAcumulados

def start_pomodoro():
    mins = 25

    while mins >= 0:
        fileOutput = open(".pomobaroutput", "w")
        fileOutput.write(" " + str(mins))
        fileOutput.close()
        # Reduce the minute total
        os.system('polybar-msg hook pomobar 1')
        # Sleep for a minute
        time.sleep(60)
        mins -= 1

    if mins <= 0:
        increment_global_pomodoro_counter()
        pomodorosAcumulados = get_pomodoros_done()
        fileOutput = open(".pomobaroutput", "w")
        fileOutput.write(" " + pomodorosAcumulados)
        fileOutput.close()
        os.system('polybar-msg hook pomobar 1')
        os.system('notify-send --urgency=normal Pomodoro finished')

def break_time():
    mins = 5

    while mins >= 0:
        fileOutput = open(".pomobaroutput", "w")
        fileOutput.write(" " + str(mins))
        fileOutput.close()
        # Reduce the minute total
        os.system('polybar-msg hook pomobar 1')
        # Sleep for a minute
        time.sleep(60)
        mins -= 1

    if mins <= 0:
        fileOutput = open(".pomobaroutput", "w")
        fileOutput.write(" pomodoro")
        fileOutput.close()
        os.system('polybar-msg hook pomobar 1')
        os.system('notify-send --urgency=low Break finished')

def kill_pomodoro():
    pomodorosAcumulados = get_pomodoros_done()
    fileOutput = open(".pomobaroutput", "w")
    fileOutput.write(" " + pomodorosAcumulados)
    fileOutput.close()
    os.system('polybar-msg hook pomobar 1')

def main():
    kill_another_instances()

    input= sys.argv[1]

    if input == "start":
        start_pomodoro()
    elif input == "break":
        break_time()
    elif input == "kill":
        kill_pomodoro()

if __name__== "__main__":
    main()
