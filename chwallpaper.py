# -*- coding: utf-8 -*-
# 
# Download and unzip Mojave dynamic background here: https://files.rb.gd/mojave_dynamic.zip 
# gsettings set org.cinnamon.desktop.background picture-uri "file:///home/tiancj/Pictures/mojave_dynamic/mojave_dynamic_16.jpeg"
# mojave_dynamic_[0:16].jpeg

import os
import sys
import time

if not os.path.exists(os.path.expanduser("~/Pictures/mojave_dynamic")):
    print("mojave_dynamic folder doesn't exist, exit")
    sys.exit(0)

pic_info = [
    [0, 7200, "mojave_dynamic_16.jpeg"],
    [2, 10800, "mojave_dynamic_16.jpeg"],
    [5, 3600, "mojave_dynamic_1.jpeg"],
    [6, 3600, "mojave_dynamic_2.jpeg"],
    [7, 3600, "mojave_dynamic_3.jpeg"],
    [8, 3600, "mojave_dynamic_4.jpeg"],
    [9, 3600, "mojave_dynamic_5.jpeg"],
    [10, 3600, "mojave_dynamic_6.jpeg"],
    [11, 7200, "mojave_dynamic_7.jpeg"],
    [13, 3600, "mojave_dynamic_8.jpeg"],
    [14, 3600, "mojave_dynamic_9.jpeg"],
    [15, 3600, "mojave_dynamic_10.jpeg"],
    [16, 3600, "mojave_dynamic_11.jpeg"],
    [17, 3600, "mojave_dynamic_12.jpeg"],
    [18, 7200, "mojave_dynamic_13.jpeg"],
    [20, 10800, "mojave_dynamic_14.jpeg"],
    [23, 3600, "mojave_dynamic_15.jpeg"],
]

BASE_FOLDER = os.path.expanduser('~/Pictures/mojave_dynamic')

while True:
    # get current hour
    t = time.localtime()
    hour = t.tm_hour
    for info in pic_info:
        if info[0] <= hour < info[0] + int(info[1]/3600):
            # found
            image = 'file://' + os.path.join(BASE_FOLDER, info[2])
            command = 'gsettings set org.cinnamon.desktop.background picture-uri ' + image
            print("command: ", command)
            os.system(command)

            # sleep
            time_to_sleep = info[1] - (hour-info[0])*3600 - t.tm_min*60
            print("sleeping: {} seconds".format(time_to_sleep))
            time.sleep(time_to_sleep)
            break

