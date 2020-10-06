input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 470000; index++) {
        music.ringTone(100000000000)
    }
})
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        basic.setLedColor(0xff0000)
        basic.pause(10)
        basic.setLedColor(0xff8000)
        basic.pause(10)
        basic.setLedColor(0xffff00)
        basic.pause(10)
        basic.setLedColor(0xff9da5)
        basic.pause(10)
        basic.setLedColor(0x00ff00)
        basic.pause(10)
        basic.setLedColor(0xb09eff)
        basic.pause(10)
        basic.setLedColor(0x00ffff)
        basic.pause(10)
        basic.setLedColor(0x007fff)
        basic.pause(10)
        basic.setLedColor(0x65471f)
        basic.pause(10)
        basic.setLedColor(0x0000ff)
        basic.pause(10)
        basic.setLedColor(0x7f00ff)
        basic.pause(10)
        basic.setLedColor(0xff0080)
        basic.pause(10)
        basic.setLedColor(0xff00ff)
        basic.pause(10)
        basic.setLedColor(0xffffff)
        basic.pause(10)
        basic.setLedColor(0x999999)
        basic.pause(10)
        basic.setLedColor(0x000000)
    }
})
basic.forever(function () {
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # .
        # # # . .
        # # . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # .
        # # # . .
        # # . . .
        # . . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # .
        # # # . .
        # # . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # .
        # # # . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # # . . .
        # . . . .
        . . # . .
        . . . . #
        . . . # #
        `)
    basic.showLeds(`
        # # . # #
        # . . . #
        . . # . .
        # . . . #
        # # . # #
        `)
    basic.showLeds(`
        # # . # #
        # . # . #
        . # # # .
        # . # . #
        # # . # #
        `)
})
