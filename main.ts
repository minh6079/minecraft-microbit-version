input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    blockLeft = !blockLeft
    Block_left()
})
function Render() {
    for (let index = 0; index < 5; index++) {
        led.plot(index, 4)
    }
    led.unplot(clear_x, 3)
    led.unplot(clear_x, 2)
    led.plot(walk, 3)
    led.plot(walk, 2)
}

input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    if (walk > 0) {
        walk += -1
        clear_x = walk + 1
    }
    
    Render()
})
function Block_left() {
    if (walk == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            # # # # #
            `)
    } else if (walk == 1) {
        led.toggle(0, 3)
    } else if (walk == 2) {
        led.toggle(1, 3)
    } else if (walk == 3) {
        led.toggle(2, 3)
    } else {
        led.toggle(3, 3)
    }
    
}

function Startup() {
    for (let index2 = 0; index2 < 8; index2++) {
        basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `, 150)
        basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `, 150)
    }
    basic.showLeds(`
            # # # # #
            # # # # #
            # # . # #
            # # # # #
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            # # # # #
            # . . . #
            # # # # #
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            # # # . #
            # . . . #
            # . # # #
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            # # . . #
            # . . . #
            # . . # #
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            . . . . #
            # . . . #
            # . . . .
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            . . . . #
            . . . . .
            # . . . .
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `, 150)
    basic.showLeds(`
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            `, 150)
    basic.showLeds(`
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            `, 150)
    basic.showLeds(`
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . # #
            `, 150)
    basic.showLeds(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `, 150)
    basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `, 150)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    blockRight = !blockRight
    Block_right()
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    if (walk < 5) {
        walk += 1
        clear_x = walk - 1
    }
    
    Render()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    led.unplot(walk, 1)
    led.plot(walk, 3)
    basic.pause(200)
    led.unplot(walk, 3)
    led.plot(walk, 1)
})
function Block_right() {
    if (walk == 0) {
        led.toggle(1, 3)
    } else if (walk == 1) {
        led.toggle(2, 3)
    } else if (walk == 2) {
        led.toggle(3, 3)
    } else if (walk == 3) {
        led.toggle(4, 3)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            # # # # #
            `)
    }
    
}

let clear_x = 0
let walk = 0
let blockLeft = false
let blockRight = false
Startup()
blockRight = false
blockLeft = false
walk = 0
Render()
