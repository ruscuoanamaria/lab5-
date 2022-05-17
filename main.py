lumiere = 0
humidity = 0

def on_logo_pressed():
    global lumiere
    lumiere = 120
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global humidity
    if input.button_is_pressed(Button.A):
        basic.show_number(input.temperature())
    elif input.light_level() > 10 and input.light_level() < 18:
        basic.show_string("Watering the plant")
    else:
        if input.button_is_pressed(Button.B):
            humidity = randint(0, 100)
            if humidity < 60:
                basic.show_string("Watering the plant")
            else:
                if humidity > 70:
                    basic.show_string("Stop watering the plant")
basic.forever(on_forever)

def on_forever2():
    temperature = 0
    if input.is_gesture(Gesture.SHAKE) and temperature > 120:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        if temperature < 120:
            basic.show_string("La pompe s arrete")
basic.forever(on_forever2)
