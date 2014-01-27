#!/usr/bin/env python

import time, os

## For simplicity's sake, we'll create a strings and filenames for our paths
ADC_PATH= os.path.normpath('/proc/')
ADC_FILENAME = "adc"
PWM_PATH= os.path.normpath('/sys/class/leds/')
PWM_DIR = "pwm"
PWM_FILENAME = "brightness"
PWM_MAX = "max_brightness"

## create empty arrays to store the pointers for our files
adcFiles = []

## Populate the arrays with paths that we can use later.
for i in range(0,6):
  adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+str(i)))

## Reading ADC values is a little more straightforward than PWM- it's just
##   classic OS file reads. Note that the value that comes out of the file is
##   a string, so you'll need to format it with int() if you want to do math
##   with that value later on!
for file in adcFiles:
  fd = open(file, 'r')
  fd.seek(0)
  print "ADC Channel: " + str(adcFiles.index(file)) + " Result: " + fd.read(16)
  fd.close()
