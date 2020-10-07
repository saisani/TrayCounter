from gpiozero import LED
from signal import pause

red = LED()

red.blink()

pause()