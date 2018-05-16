#!/bin/bash
DATE=$(date +%Y-%m-%d_%H%M)
fswebcam -r 320x240 /home/pi/webcam/$DATE.jpg
