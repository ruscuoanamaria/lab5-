let lumiere = 0
let humidity = 0
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    lumiere = 120
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(input.temperature())
    } else if (input.lightLevel() > 10 && input.lightLevel() < 18) {
        basic.showString("Watering the plant")
    } else {
        if (input.buttonIsPressed(Button.B)) {
            humidity = randint(0, 100)
            if (humidity < 60) {
                basic.showString("Watering the plant")
            } else {
                if (humidity > 70) {
                    basic.showString("Stop watering the plant")
                }
            }
        }
    }
})
basic.forever(function () {
    let temperature = 0
    if (input.isGesture(Gesture.Shake) && temperature > 120) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        if (temperature < 120) {
            basic.showString("La pompe s arrete")
        }
    }
})
