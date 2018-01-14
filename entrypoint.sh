#!/bin/bash

if [ "$SHOWHELP" == "true" ]; then
   /usr/local/bin/electricity_exporter.py -h
   exit $?
fi



if [ -z "$LISTENPORT" ]; then
    LISTENPORT=8110
fi

python /usr/local/bin/electricity_exporter.py -p $LISTENPORT

