#!/bin/bash

COMMAND=./bot.py
LOGFILE=crash.txt

writelog() {
	now=`date`
	echo "$now $*" >> $LOGFILE
}

writelog "Starting"
while true ; do
	$COMMAND
	writelog "Exited with status $?"
	writelog "Restarting"
done
