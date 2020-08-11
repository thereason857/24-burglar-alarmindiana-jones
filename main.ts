let Door_Sensor = 0
let Pressure_Sensor = 0
let Alarm = 0
function Update_Sensors () {
    Door_Sensor = pins.digitalReadPin(DigitalPin.P2)
    Pressure_Sensor = pins.digitalReadPin(DigitalPin.P1)
}
function Alarm_on_Check () {
    if (Door_Sensor == 0) {
        basic.showString("Check Doors")
    } else if (Pressure_Sensor == 0) {
        basic.showString("Check Safe")
    } else {
        Alarm = 1
    }
}
input.onButtonPressed(Button.A, function () {
    Alarm_on_Check()
})
input.onButtonPressed(Button.B, function () {
    Alarm = 0
    basic.showLeds(`
        . # . # .
        . # . # .
        # # # # #
        # # # # #
        # # # # #
        `)
})
basic.forever(function () {
    Update_Sensors()
    while (Alarm == 1 && (Door_Sensor == 1 && Pressure_Sensor == 1)) {
        basic.showLeds(`
            . # # # .
            . # . # .
            # # # # #
            # # # # #
            # # # # #
            `)
        Update_Sensors()
    }
    while (Alarm == 1 && (Door_Sensor == 0 || Pressure_Sensor == 0)) {
        basic.showIcon(IconNames.No)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.clearScreen()
        basic.pause(500)
    }
})
