def on_button_pressed_a():
    for index in range(90077777):
        music.play_tone(139, music.beat(BeatFraction.BREVE))
        music.play_tone(156, music.beat(BeatFraction.BREVE))
        music.play_tone(185, music.beat(BeatFraction.BREVE))
        music.play_tone(208, music.beat(BeatFraction.BREVE))
        music.play_tone(233, music.beat(BeatFraction.BREVE))
        music.play_tone(277, music.beat(BeatFraction.BREVE))
        music.play_tone(311, music.beat(BeatFraction.BREVE))
        music.play_tone(370, music.beat(BeatFraction.BREVE))
        music.play_tone(415, music.beat(BeatFraction.BREVE))
        music.play_tone(466, music.beat(BeatFraction.BREVE))
        music.play_tone(554, music.beat(BeatFraction.BREVE))
        music.play_tone(622, music.beat(BeatFraction.BREVE))
        music.play_tone(740, music.beat(BeatFraction.BREVE))
        music.play_tone(831, music.beat(BeatFraction.BREVE))
        music.play_tone(932, music.beat(BeatFraction.BREVE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    for index2 in range(4):
        basic.set_led_color(0xff0000)
        basic.pause(10)
        basic.set_led_color(0xff8000)
        basic.pause(10)
        basic.set_led_color(0xffff00)
        basic.pause(10)
        basic.set_led_color(0xff9da5)
        basic.pause(10)
        basic.set_led_color(0x00ff00)
        basic.pause(10)
        basic.set_led_color(0xb09eff)
        basic.pause(10)
        basic.set_led_color(0x00ffff)
        basic.pause(10)
        basic.set_led_color(0x007fff)
        basic.pause(10)
        basic.set_led_color(0x65471f)
        basic.pause(10)
        basic.set_led_color(0x0000ff)
        basic.pause(10)
        basic.set_led_color(0x7f00ff)
        basic.pause(10)
        basic.set_led_color(0xff0080)
        basic.pause(10)
        basic.set_led_color(0xff00ff)
        basic.pause(10)
        basic.set_led_color(0xffffff)
        basic.pause(10)
        basic.set_led_color(0x999999)
        basic.pause(10)
        basic.set_led_color(0x000000)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # .
        # # # . .
        # # . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        # # # # .
        # # # . .
        # # . . .
        # . . . .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # .
        # # # . .
        # # . . .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # .
        # # # . .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        # # . . .
        # . . . .
        . . # . .
        . . . . #
        . . . # #
        """)
    basic.show_leds("""
        # # . # #
        # . . . #
        . . # . .
        # . . . #
        # # . # #
        """)
    basic.show_leds("""
        # # . # #
        # . # . #
        . # # # .
        # . # . #
        # # . # #
        """)
basic.forever(on_forever2)
