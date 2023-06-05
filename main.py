from machine import Pin, Signal
from machine import Timer
import time

# D8 D7 D6 D5 D0 = 15 13 12 14 16
# D4 D3 D2 D1    = 2 0 4 5
# I2C   = D1 D2
# WAKE  = D0
# FLASH = D3

BTN_PIN_NO = [13, 12, 14]
LED_PIN_NO = 2

button_info = []

# https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.Signal.html#machine-signal

pin = Pin(LED_PIN_NO, Pin.OUT)
led = Signal(pin, invert=True)  # LEDピンは論理反転している


class ActionButton():

    def __init__(self, id:int, pin_no: int, signal:Signal):
        self.id = id
        self.pin_no = pin_no
        self.signal:Signal = signal

    def button_push_handler(self):
        print(f"button pushed {self.id}")
        led.on()
        time.sleep_ms(500)
        led.off()


def periodic_log_handler(t):
    import time
    print(f"Still running. { time.ticks_ms() }")


for i, pin_no in enumerate(BTN_PIN_NO):
    pin = Pin(pin_no, Pin.IN, Pin.PULL_UP)
    btn = Signal(pin, invert=True)

    button_info.append(ActionButton(i, pin_no, btn))


for i in range(5):
    led.on()
    time.sleep_ms(200)
    led.off()
    time.sleep_ms(200)

print("Start up completed.")

# async timer
timer = Timer(-1)
timer.init(period=5000, mode=Timer.PERIODIC, callback=periodic_log_handler)

while True:
    for i, btn in enumerate(button_info):
        if btn.signal.value() == 1:
            btn.button_push_handler()

    time.sleep_ms(50)
