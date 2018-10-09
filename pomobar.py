#!/usr/bin/python3
##############################
# AUTHOR: Antonio Alonso
# DATE: 2018-10-09
# DESCRIPTION:
# TODO: pending
# contador de pomododrso global
# subirlo a githb
##############################
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

def start_pomodoro():
    mins = 25

    while mins >= 0:
        fileOutput = open("pomobaroutput", "w")
        fileOutput.write(" " + str(mins))
        fileOutput.close()
        # Reduce the minute total
        os.system('polybar-msg hook pomobar 1')
        # Sleep for a minute
        time.sleep(60)
        mins -= 1

    if mins <= 0:
        fileOutput = open("pomobaroutput", "w")
        fileOutput.write(" pomodoro")
        fileOutput.close()
        os.system('polybar-msg hook pomobar 1')

def break_time():
    mins = 5

    while mins >= 0:
        fileOutput = open("pomobaroutput", "w")
        fileOutput.write(" " + str(mins))
        fileOutput.close()
        # Reduce the minute total
        os.system('polybar-msg hook pomobar 1')
        # Sleep for a minute
        time.sleep(60)
        mins -= 1

    if mins <= 0:
        fileOutput = open("pomobaroutput", "w")
        fileOutput.write(" pomodoro")
        fileOutput.close()
        os.system('polybar-msg hook pomobar 1')

def kill_pomodoro():
    fileOutput = open("pomobaroutput", "w")
    fileOutput.write(" pomodoro")
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
