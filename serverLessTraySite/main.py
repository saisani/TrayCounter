import logging as log
import os
import webview

from api import API

# file paths
LOG_FILE_PATH = "debug.log"
HTML_FILES = "assets/index.html"
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
GPIO_PIN = 4

# initialize class
api = API(GPIO_PIN)

def clear_debug_log(logfile):
    f = open(logfile, "w").close()

def configure_logging(logfile):
    log.basicConfig(filename=logfile, 
                    level=log.INFO, 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d %I:%M:%S')

def start_hardware():
    log.debug("Starting Hardware")
    api.setupSensor()

def start_webpage():
    log.debug("Starting Webpage")
    api.addWindow(webview.create_window("", HTML_FILES, 
        js_api=api, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, 
        fullscreen=True, frameless=True))
    webview.start(gui='gtk')

def stop():
    pass

def main():
    pass

if __name__ == '__main__':
    clear_debug_log(LOG_FILE_PATH)
    configure_logging(LOG_FILE_PATH)
    start_hardware()
    start_webpage()
    main()
