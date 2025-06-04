def on_button_pressed_a():
    global blockLeft
    blockLeft = not (blockLeft)
    Block_left()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Render():
    for index in range(5):
        led.plot(index, 4)
    led.unplot(clear_x, 3)
    led.unplot(clear_x, 2)
    led.plot(walk, 3)
    led.plot(walk, 2)

def on_gesture_tilt_left():
    global walk, clear_x
    if walk > 0:
        walk += -1
        clear_x = walk + 1
    Render()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def Block_left():
    if walk == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            # # # # #
            """)
    elif walk == 1:
        led.toggle(0, 3)
    elif walk == 2:
        led.toggle(1, 3)
    elif walk == 3:
        led.toggle(2, 3)
    else:
        led.toggle(3, 3)
def Startup():
    for index2 in range(8):
        basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """,
            150)
        basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """,
            150)
    basic.show_leds("""
            # # # # #
            # # # # #
            # # . # #
            # # # # #
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            # # # # #
            # . . . #
            # # # # #
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            # # # . #
            # . . . #
            # . # # #
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            # # . . #
            # . . . #
            # . . # #
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            . . . . #
            # . . . #
            # . . . .
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            . . . . #
            . . . . .
            # . . . .
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """,
        150)
    basic.show_leds("""
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            """,
        150)
    basic.show_leds("""
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            """,
        150)
    basic.show_leds("""
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . # #
            """,
        150)
    basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """,
        150)
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """,
        150)

def on_button_pressed_b():
    global blockRight
    blockRight = not (blockRight)
    Block_right()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global walk, clear_x
    if walk < 5:
        walk += 1
        clear_x = walk - 1
    Render()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_logo_pressed():
    led.unplot(walk, 1)
    led.plot(walk, 3)
    basic.pause(200)
    led.unplot(walk, 3)
    led.plot(walk, 1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def Block_right():
    if walk == 0:
        led.toggle(1, 3)
    elif walk == 1:
        led.toggle(2, 3)
    elif walk == 2:
        led.toggle(3, 3)
    elif walk == 3:
        led.toggle(4, 3)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            # # # # #
            """)
clear_x = 0
walk = 0
blockLeft = False
blockRight = False
Startup()
blockRight = False
blockLeft = False
walk = 0
Render()