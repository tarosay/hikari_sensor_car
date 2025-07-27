動く右 = 0
動く左 = 0
P13_PWM = 0
P16_PWM = 0
矢印前 = 0
def 動く(右タイヤ: number, 左タイヤ: number):
    global 動く右, 動く左, P13_PWM, P16_PWM
    if 右タイヤ >= 0:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        動く右 = 右タイヤ
    else:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P9, 0)
        動く右 = 0 - 右タイヤ
    if 左タイヤ >= 0:
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.digital_write_pin(DigitalPin.P15, 1)
        動く左 = 左タイヤ
    else:
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P15, 0)
        動く左 = 0 - 左タイヤ
    P13_PWM = 1023 * (動く左 / 100)
    if P13_PWM > 1023:
        P13_PWM = 1023
    P16_PWM = 1023 * (動く右 / 100)
    if P16_PWM > 1023:
        P16_PWM = 1023
    pins.analog_write_pin(AnalogPin.P13, P13_PWM)
    pins.analog_write_pin(AnalogPin.P16, P16_PWM)

def on_forever():
    global 矢印前
    if input.light_level() >= 100:
        if 矢印前 == 0:
            矢印前 = 1
            basic.show_arrow(ArrowNames.NORTH)
        動く(80, 80)
    else:
        動く(60, -60)
        basic.pause(150)
        動く(0, 0)
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            . . # . #
            . # # # .
            """)
        矢印前 = 0
        basic.pause(500)
basic.forever(on_forever)
