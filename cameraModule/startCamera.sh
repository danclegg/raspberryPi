#!/bin/bash

rm -f *.jpg && rm -f *.avi && ls

sudo service motion start

sudo python turnOffCameraLight.py

