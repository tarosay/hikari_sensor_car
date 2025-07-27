let 動く右 = 0
let 動く左 = 0
function 動く (右タイヤ: number, 左タイヤ: number) {
    if (右タイヤ >= 0) {
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 1)
        動く右 = 右タイヤ
    } else {
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P9, 0)
        動く右 = 0 - 右タイヤ
    }
    if (左タイヤ >= 0) {
        pins.digitalWritePin(DigitalPin.P14, 0)
        pins.digitalWritePin(DigitalPin.P15, 1)
        動く左 = 左タイヤ
    } else {
        pins.digitalWritePin(DigitalPin.P14, 1)
        pins.digitalWritePin(DigitalPin.P15, 0)
        動く左 = 0 - 左タイヤ
    }
    pins.analogWritePin(AnalogPin.P13, 動く左)
    pins.analogWritePin(AnalogPin.P16, 動く右)
}
basic.forever(function () {
    動く(200, -200)
    basic.pause(300)
    動く(0, 0)
    basic.pause(500)
})
