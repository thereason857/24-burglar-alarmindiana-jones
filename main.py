Door_Sensor = 0
Pressure_Sensor = 0
Alarm = 0
def Alarm_on_Check():
    global Alarm
    if Door_Sensor == 0:
        basic.show_string("Check Doors")
    elif Pressure_Sensor == 0:
        basic.show_string("Check Safe")
    else:
        Alarm = 1

def on_button_pressed_a():
    Alarm_on_Check()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Update_Sensors():
    global Door_Sensor, Pressure_Sensor
    Door_Sensor = pins.digital_read_pin(DigitalPin.P2)
    Pressure_Sensor = pins.digital_read_pin(DigitalPin.P1)

def on_button_pressed_b():
    global Alarm
    Alarm = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    Update_Sensors()
    while Alarm == 1 and (Door_Sensor == 1 and Pressure_Sensor == 1):
        basic.show_leds("""
            . # # # .
            . # . # .
            # # # # #
            # # # # #
            # # # # #
            """)
        Update_Sensors()
    while Alarm == 1 and (Door_Sensor == 0 or Pressure_Sensor == 0):
        basic.show_icon(IconNames.NO)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.clear_screen()
        basic.pause(500)
basic.forever(on_forever)
