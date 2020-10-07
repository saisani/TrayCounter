"""
Use this program to develop on x86 due to lack of RPi libraries
"""
import logging as log
import os
import requests
from playsound import playsound
import urllib
import webview

# write to different day file paths

# file paths
LOG_FILE_PATH = "debug.log"
HTML_FILES = "assets/index.html"
SOUND_FILE = "sounds/microwave_beep.wav"
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
GPIO_PIN = 17

# plays beep synchronously
def play_beep():
    playsound(SOUND_FILE)

# class to interact with js in web page
class Api:
    def __init__(self):
        self._count = 0
        self._foundTray = False

    def setupWindow(self):
        self._window = webview.create_window("", 
            HTML_FILES, 
            js_api=api, 
            width=WINDOW_WIDTH, 
            height=WINDOW_HEIGHT, 
            fullscreen=True)
    
    def setCount(self, count):
        prev_count = self._count
        if count>=0 and count<999:
            self._count = count
            play_beep()
        if prev_count != count:
            log.info("Count has changed from %i to %i", prev_count, self._count)

    def beginTray(self):
        self._foundTray = True
        log.debug("Starting tray at %i trays left", self._count)

    def endTray(self):
        if self._foundTray:
            log.debug("Ending tray at %i trays left", self._count)
            self.updateCount()
            self._foundTray = False
        else:
            log.debug("Weird tray detection at the beginning but not at the end")

    def updateCount(self):
        prev_count = self._count
        self._count -= 1

        js_code = r"""
            var calcText = document.getElementById('calc-textbox');
            calcText.value = '{}';
        """.format(self._count)
        self._window.evaluate_js(js_code)

        log.debug("Count has decreased from %i to %i", prev_count, self._count)

    def getWifiStatus(self):
        try:
            url = "https://www.google.com"
            requests.get(url)
            return {'status': True}
        except:
            return {'message': False}

    def turnOff(self):
        print("Starting shut down on current device")


# initialize class
api = Api()

def configure_logging(logfile):
    log.basicConfig(filename=logfile, 
                    level=log.DEBUG, 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d %I:%M:%S')

def start_hardware():
    log.debug("Starting Hardware")

def start_webpage():
    log.debug("Starting Webpage")
    api.setupWindow()
    webview.start(gui='gtk')

def stop():
    pass

def main():
    pass

if __name__ == '__main__':
    configure_logging(LOG_FILE_PATH)
    start_hardware()
    start_webpage()
    main()
