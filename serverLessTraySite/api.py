"""
API to interact between client (JS/html page) and the client (python program)
"""
from gpiozero import LineSensor
import logging as log
import requests
import os
import webview

MIN_COUNT = 0
MAX_COUNT = 999

class API:
    def __init__(self, gpio_pin):
        self._count = 0
        self._foundTray = False
        self._sensor = None
        self._window = None

        self.gpio_pin = gpio_pin

    def addWindow(self, window):
        self._window = window

    def setupSensor(self):
        self._sensor = LineSensor(self.gpio_pin)
        self._sensor.when_activated = self.beginTray
        self._sensor.when_deactivated = self.endTray

    def setCount(self, count):
        prev_count = self._count
        if count <= MIN_COUNT:
            self._count = MIN_COUNT
        elif count > MAX_COUNT:
            self._count = MAX_COUNT
        else:
            self._count = count
        log.info("Count has been set to %i", self._count)

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
        if prev_count > MIN_COUNT:
            self._count -= 1

        js_code = r"""
            var calcText = document.getElementById('calc-textbox');
            calcText.value = '{}';
        """.format(self._count)
        self._window.evaluate_js(js_code)

        log.info("Count has decreased from %i to %i", prev_count, self._count)

    def getWifiStatus(self):
        try:
            url = "https://www.google.com"
            requests.get(url)
            return {'status': True}
        except:
            return {'message': False}

    def turnOff(self):
        log.debug("Shutting down Raspberry Pi")
        os.system("shutdown -P now")
