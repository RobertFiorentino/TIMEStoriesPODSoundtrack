#! /usr/bin/env/python3

# Prophecy of Dragons background music script

import webbrowser, sys, time
from selenium import webdriver


# check if any arguments were passed
if len(sys.argv) < 2:
    print("Program exiting because no location was passed in.")
    sys.exit()

# create mapping for arguments and links
songMap = {"base" : "93",
           "dragon inn" : "23",
           "market" : "56",
           "old dock" : "75",
           "castle plaza" : "104",
           "lost woods" : "69",
           "location 2" : "13",
           "2" : "13",
           "location 3" : "20",
           "3" : "20",
           "location 6" : "10",
           "6" : "10",
           "location 7" : "85",
           "7" : "85",
           "location 9" : "42",
           "9" : "42",
           "guard room" : "78",
           "ballroom" : "71",
           "ball room" : "71",
           "archives" : "28",
           "library" : "73",
           "location 11" : "34",
           "11" : "34",
           "location 17" : "65",
           "17" : "65"}
           
# get the link from the argument, exit if not in list
argString = " ".join(sys.argv[1:])
if argString.lower() not in songMap:
    print("Program exiting because \"" + argString + "\" is not in the song mapping.")
    sys.exit()

# concatenate song number with link
link = "http://tabletopaudio.com/index.html?" + songMap[argString.lower()]

# open the link
browser = webdriver.Chrome()
browser.get(link)


# press play
elem = browser.find_element_by_css_selector("#jp_container_1 > div.jp-type-playlist > div.jp-gui.jp-interface > ul.jp-controls > li:nth-child(1) > button > span")
time.sleep(1)
elem.click()
