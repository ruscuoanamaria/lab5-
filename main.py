def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_number(input.temperature()) #display the temperature
    elif input.light_level() > 10: #check the light level
        basic.show_icon(IconNames.HEART)
    else:
        basic.clear_screen()
 
basic.forever(on_forever)