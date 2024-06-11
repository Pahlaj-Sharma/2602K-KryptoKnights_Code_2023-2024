# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Pahlaj Sharma - 2602K KryptoKnights - 2023-2024              #
# 	Created:      9/23/2023, 11:22:20 AM                                       #
# 	Description:  Robot Code for 2602K KryptoKnights                           #
#   Version:      V2.72                                                        #
#                                                                              #
# ---------------------------------------------------------------------------- #

from vex import *

brain=Brain()

FrontRight = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
MiddleRight = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
BackRight = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
FrontLeft = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
MiddleLeft = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
BackLeft = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
controller_1 = Controller(PRIMARY)
Catapult = Motor(Ports.PORT13, GearSetting.RATIO_36_1, True)
Catapult2 = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
Intake = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
FrontWingsPneumatic = DigitalOut(brain.three_wire_port.h)
inertial_gyro = Inertial(Ports.PORT20)
AutonSelector = Limit(brain.three_wire_port.e)
HangPneumatic = DigitalOut(brain.three_wire_port.c)
BackWingPneumaticR = DigitalOut(brain.three_wire_port.d)
BackWingPneumaticL = DigitalOut(brain.three_wire_port.g)
SideHangPneumatic = DigitalOut(brain.three_wire_port.f)

wait(230, MSEC)
print("\033[2J")
brain.screen.clear_screen()
controller_1.screen.clear_screen()

Deadband = 5
vexcode_brain_precision = 0
vexcode_console_precision = 0
WingsPressed = False
HangPressed = False
BackWingsPressed = False
SideHang = False

def when_started1():
    global Deadband, vexcode_brain_precision, vexcode_console_precision
    FrontRight.set_stopping(COAST)
    MiddleRight.set_stopping(COAST)
    BackRight.set_stopping(COAST)
    FrontLeft.set_stopping(COAST)
    MiddleLeft.set_stopping(COAST)
    BackLeft.set_stopping(COAST)
    controller_1.screen.print("Driving Skills")

def onauton_autonomous_0():
    pass

def ondriver_drivercontrol_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    FrontWingsPneumatic.set(False)
    BackWingPneumaticL.set(False)
    BackWingPneumaticR.set(False)
    while True:
        if math.fabs(controller_1.axis1.position()) + math.fabs(controller_1.axis3.position()) > Deadband:
            if math.fabs(controller_1.axis1.position()) > -360 and math.fabs(controller_1.axis1.position()) < 360:
                #turning
                FrontRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                MiddleRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                BackRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                FrontLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                MiddleLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                BackLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
            elif math.fabs(controller_1.axis3.position()) > 0 and math.fabs(controller_1.axis3.position()) < 180:
                #forward
                FrontRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                MiddleRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                BackRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                FrontLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                MiddleLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                BackLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)  
        else:
            FrontRight.set_velocity(0, RPM)
            MiddleRight.set_velocity(0, RPM)
            BackRight.set_velocity(0, RPM)
            FrontLeft.set_velocity(0, RPM)
            MiddleLeft.set_velocity(0, RPM)
            BackLeft.set_velocity(0, RPM)
        FrontRight.spin(REVERSE)
        MiddleRight.spin(REVERSE)
        BackRight.spin(REVERSE)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        wait(10, MSEC)

def onevent_controller_1buttonL2_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #wings out/in
    if WingsPressed == True:
        FrontWingsPneumatic.set(False)
        WingsPressed = False
    else:
        FrontWingsPneumatic.set(True)
        WingsPressed = True

def onevent_controller_1buttonR2_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, BackWingsPressed
    #wings out/in
    if BackWingsPressed == True:
        BackWingPneumaticR.set(False)
        BackWingPneumaticL.set(False)
        BackWingsPressed = False
    else:
        BackWingPneumaticR.set(True)
        BackWingPneumaticL.set(True)
        BackWingsPressed = True

def onevent_controller_1buttonR1_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #matchload
    Catapult.set_velocity(63, RPM)
    Catapult2.set_velocity(63, RPM)
    Catapult.set_stopping(COAST)
    Catapult2.set_stopping(COAST)
    Catapult.spin(FORWARD)
    Catapult2.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    while not controller_1.buttonR1.pressing():
        wait(5, MSEC)
    Catapult.stop()
    Catapult2.stop()
    wait(200, MSEC)
    
def onevent_controller_1buttonL1_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #outake
    Intake.stop()
    Intake.set_velocity(180, RPM)
    Intake.spin(REVERSE)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    while not controller_1.buttonL1.pressing():
        wait(5, MSEC)
    Intake.stop()

def onevent_controller_1buttonY_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #intake
    Intake.set_stopping(COAST)
    Intake.set_velocity(180, RPM)
    Intake.spin(FORWARD)
    while not controller_1.buttonL1.pressing():
        wait(5, MSEC)
    Intake.stop()
    
def onevent_controller_1buttonRight_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, HangPressed
    brain.timer.clear()
    #hang up/down
    if HangPressed == True:
        HangPneumatic.set(False)
        HangPressed = False
    else:
        HangPneumatic.set(True)
        HangPressed = True
        
def onevent_controller_1buttonLeft_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, HangPressed, SideHang
    brain.timer.clear()
    #sidehang up/down
    if SideHang == True:
        SideHangPneumatic.set(False)
        SideHang = False
    else:
        SideHangPneumatic.set(True)
        SideHang = True

def vexcode_auton_function():
    auton_task_0 = Thread(onauton_autonomous_0)
    while(competition.is_autonomous() and competition.is_enabled()):
        wait(10, MSEC)
    auton_task_0.stop()

def vexcode_driver_function():
    driver_control_task_0 = Thread(ondriver_drivercontrol_0)
    while(competition.is_driver_control() and competition.is_enabled()):
        wait(10, MSEC)
    driver_control_task_0.stop()

competition = Competition(vexcode_driver_function, vexcode_auton_function)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)
controller_1.buttonRight.pressed(onevent_controller_1buttonRight_pressed_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonLeft.pressed(onevent_controller_1buttonLeft_pressed_0)
when_started1()