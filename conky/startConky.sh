#!/bin/bash
killall conky
sleep 1s
conky -c /home/mjalmonte/.config/conky/default.conkyrc
